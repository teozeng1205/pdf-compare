#!/usr/bin/env python3
"""
AI Models Airline Insights Comparison Dashboard
Integrates JSON insights with cropped visualizations
"""

import streamlit as st
import json
import os
import base64
from pathlib import Path
import re

# Configure page
st.set_page_config(
    page_title="AI Models vs Images Comparison", 
    page_icon="✈️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
        border-bottom: 3px solid #1f4e79;
        padding-bottom: 1rem;
    }
    .model-tag {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        color: white;
        text-transform: uppercase;
    }
    .gpt-4o { background: linear-gradient(135deg, #FF6B6B, #FF8E8E); }
    .gpt-4o-mini { background: linear-gradient(135deg, #4ECDC4, #7ED7D1); }
    .o1 { background: linear-gradient(135deg, #45B7D1, #73C5DE); }
    .o3 { background: linear-gradient(135deg, #96CEB4, #AED6C7); }
    .o3-mini { background: linear-gradient(135deg, #FFEAA7, #FFE4A7); color: #2d3436; }
    
    .insight-content {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #4CAF50;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .section-header {
        color: #1565C0;
        font-weight: bold;
        font-size: 1.2rem;
        margin: 1rem 0;
        padding: 0.5rem;
        background: linear-gradient(90deg, #e3f2fd 0%, #ffffff 100%);
        border-radius: 5px;
    }
    .image-container {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #fafafa;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_insights_data():
    """Load all insights data from JSON files"""
    base_path = Path("specified_models_run_20250715_230613")
    models = ["gpt-4o", "gpt-4o-mini", "o1", "o3", "o3-mini"]
    
    data = {}
    airlines = set()
    
    for model in models:
        model_path = base_path / f"insights_{model}"
        if model_path.exists():
            data[model] = {}
            for json_file in model_path.glob("*.json"):
                airline_code = json_file.stem.split("_")[0]
                airlines.add(airline_code)
                
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data[model][airline_code] = json.load(f)
                except Exception as e:
                    st.error(f"Error loading {json_file}: {e}")
    
    return data, sorted(list(airlines))

def get_available_images():
    """Get all available cropped images organized by airline and type"""
    cropped_path = Path("cropped")
    if not cropped_path.exists():
        return {}
    
    images = {}
    for img_file in cropped_path.glob("*.png"):
        # Parse filename: cropped_AA-OTA1-Compare_Live_Site_to_OTA-all.png
        name_parts = img_file.stem.replace("cropped_", "").split("-")
        if len(name_parts) >= 3:
            airline = name_parts[0]
            channel = name_parts[1][:3]  # OTA, MSE, GDS
            analysis_type = name_parts[-1]  # all, region, poo, booking_window
            
            if airline not in images:
                images[airline] = {}
            if channel not in images[airline]:
                images[airline][channel] = {}
            
            images[airline][channel][analysis_type] = str(img_file)
    
    return images

def display_image(image_path):
    """Display an image in Streamlit"""
    if os.path.exists(image_path):
        st.image(image_path, use_column_width=True)
    else:
        st.warning(f"Image not found: {image_path}")

def map_section_to_image_type(section_name):
    """Map JSON section names to image analysis types"""
    mapping = {
        "ota_highlights": "all",
        "mse_highlights": "all", 
        "gds_highlights": "all",
        "ota_summary_high_level_comparison": "all",
        "mse_summary_high_level_comparison": "all",
        "gds_summary_high_level_comparison": "all",
        "ota_summary_by_region": "region",
        "mse_summary_by_region": "region",
        "gds_summary_by_region": "region",
        "ota_summary_by_point_of_origin": "poo",
        "mse_summary_by_point_of_origin": "poo", 
        "gds_summary_by_point_of_origin": "poo",
        "ota_summary_by_booking_window": "booking_window",
        "mse_summary_by_booking_window": "booking_window",
        "gds_summary_by_booking_window": "booking_window"
    }
    return mapping.get(section_name, "all")

def get_channel_from_section(section_name):
    """Extract channel (OTA/MSE/GDS) from section name"""
    if "ota" in section_name.lower():
        return "OTA"
    elif "mse" in section_name.lower():
        return "MSE" 
    elif "gds" in section_name.lower():
        return "GDS"
    return None

def display_insights_with_image(airline_data, section_name, section_title, airline_code, available_images):
    """Display AI insights alongside corresponding image"""
    
    # Get corresponding image
    channel = get_channel_from_section(section_name)
    image_type = map_section_to_image_type(section_name)
    
    image_path = None
    if (airline_code in available_images and 
        channel in available_images[airline_code] and 
        image_type in available_images[airline_code][channel]):
        image_path = available_images[airline_code][channel][image_type]
    
    # Layout: Image on left, AI insights on right
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📊 Data Visualization")
        if image_path:
            display_image(image_path)
            st.caption(f"{channel} Analysis - {image_type.replace('_', ' ').title()}")
        else:
            st.info(f"No visualization available for {airline_code} - {channel} - {image_type}")
    
    with col2:
        st.markdown(f"### 🤖 AI Model Insights: {section_title}")
        
        # Get models with data for this section
        models_with_data = []
        for model, data in airline_data.items():
            if data and section_name in data:
                models_with_data.append(model)
        
        if not models_with_data:
            st.warning("No AI insights available for this section")
            return
        
        # Display each model's insights
        for model in models_with_data:
            st.markdown(f'<span class="model-tag {model.replace("-", "-")}">{model}</span>', 
                       unsafe_allow_html=True)
            
            section_data = airline_data[model][section_name]
            
            for item in section_data:
                title = item.get('line_title', '')
                content = item.get('line_content', '')
                
                insight_text = ""
                if title:
                    insight_text += f"**{title}**\n\n"
                insight_text += content
                
                st.markdown(f'<div class="insight-content">{insight_text}</div>', 
                           unsafe_allow_html=True)
            
            st.markdown("---")

def main():
    # Header
    st.markdown('<h1 class="main-header">✈️ AI Models vs Data Visualizations</h1>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    **Compare AI model insights with actual data visualizations side-by-side**
    
    This dashboard shows AI-generated insights alongside the corresponding charts and graphs for validation.
    """)
    
    # Load data
    with st.spinner("Loading data and images..."):
        insights_data, airlines = load_insights_data()
        available_images = get_available_images()
    
    if not insights_data:
        st.error("No insights data found. Please check the data directory structure.")
        return
    
    if not available_images:
        st.error("No images found in cropped/ directory.")
        return
    
    # Find common airlines between insights and images
    common_airlines = set(airlines) & set(available_images.keys())
    if not common_airlines:
        st.error("No common airlines found between insights and images.")
        return
    
    # Sidebar
    st.sidebar.title("🎛️ Controls")
    
    # Airline selection (only show airlines with both data and images)
    selected_airline = st.sidebar.selectbox(
        "✈️ Select Airline",
        sorted(list(common_airlines)),
        help="Airlines with both AI insights and visualizations"
    )
    
    # Show available channels for selected airline
    if selected_airline and selected_airline in available_images:
        available_channels = list(available_images[selected_airline].keys())
        st.sidebar.markdown(f"**Available channels for {selected_airline}:** {', '.join(available_channels)}")
    
    # Section selection - filter by available images
    all_sections = [
        ("ota_highlights", "🌐 OTA Highlights"),
        ("ota_summary_high_level_comparison", "📊 OTA High-Level Comparison"),
        ("ota_summary_by_region", "🌍 OTA by Region"),
        ("ota_summary_by_point_of_origin", "📍 OTA by Origin"),
        ("ota_summary_by_booking_window", "⏰ OTA by Booking Window"),
        ("mse_highlights", "🔍 MSE Highlights"),
        ("mse_summary_high_level_comparison", "📊 MSE High-Level Comparison"),
        ("mse_summary_by_region", "🌍 MSE by Region"),
        ("mse_summary_by_point_of_origin", "📍 MSE by Origin"),
        ("mse_summary_by_booking_window", "⏰ MSE by Booking Window"),
        ("gds_highlights", "💼 GDS Highlights"),
        ("gds_summary_high_level_comparison", "📊 GDS High-Level Comparison"),
        ("gds_summary_by_region", "🌍 GDS by Region"),
        ("gds_summary_by_point_of_origin", "📍 GDS by Origin"),
        ("gds_summary_by_booking_window", "⏰ GDS by Booking Window")
    ]
    
    # Filter sections based on available images for selected airline
    available_sections = []
    if selected_airline and selected_airline in available_images:
        for section_code, section_title in all_sections:
            channel = get_channel_from_section(section_code)
            image_type = map_section_to_image_type(section_code)
            
            if (channel in available_images[selected_airline] and 
                image_type in available_images[selected_airline][channel]):
                available_sections.append((section_code, section_title))
    
    if not available_sections:
        st.warning("No matching sections found for selected airline.")
        return
    
    selected_section = st.sidebar.selectbox(
        "📋 Select Analysis Section",
        [s[0] for s in available_sections],
        format_func=lambda x: next(s[1] for s in available_sections if s[0] == x),
        help="Sections with both AI insights and visualizations"
    )
    
    # Model selection
    available_models = list(insights_data.keys())
    selected_models = st.sidebar.multiselect(
        "🤖 Select AI Models",
        available_models,
        default=available_models,
        help="Choose which AI models to include"
    )
    
    # Main content
    if selected_airline and selected_section and selected_models:
        section_title = next(s[1] for s in available_sections if s[0] == selected_section)
        
        # Prepare data for selected airline and models
        airline_data = {}
        for model in selected_models:
            airline_data[model] = insights_data.get(model, {}).get(selected_airline, None)
        
        # Display insights with corresponding image
        display_insights_with_image(
            airline_data, 
            selected_section, 
            section_title, 
            selected_airline, 
            available_images
        )
    
    # Footer
    st.markdown("---")
    st.markdown(
        f"""
        <div style='text-align: center; color: #666; padding: 1rem;'>
            <p>📊 AI Models vs Data Visualizations Dashboard</p>
            <p>Comparing AI insights with actual data charts for {len(common_airlines)} airlines</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 