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
    page_icon=None, 
    layout="centered", # Changed to centered layout for more compactness
    initial_sidebar_state="expanded"
)

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
    col1, col2 = st.columns([0.1, 1.9]) # Adjusted column ratio for maximum compactness
    
    with col1:
        if image_path:
            st.image(image_path, use_column_width=True)
        else:
            pass
    
    with col2:
        # Get models with data for this section
        models_with_data = []
        for model, data in airline_data.items():
            if data and section_name in data:
                models_with_data.append(model)
        
        if not models_with_data:
            pass # Removed warning for compactness
        
        # Display each model's insights
        for model in models_with_data:
            section_data = airline_data[model][section_name]
            
            model_insights_text = []
            for item in section_data:
                title = item.get('line_title', '')
                content = item.get('line_content', '')
                
                insight_text = ""
                if title:
                    insight_text += f"{title}: "
                insight_text += content
                model_insights_text.append(insight_text)
            
            # Display model name and insights on a single line where possible, or with minimal newlines
            st.text(f"Model {model.upper()}: " + " ".join(model_insights_text).replace("\n", " "))

def main():
    # Header
    # Removed header for compactness
    # st.markdown("## AI Models vs Data Visualizations") 
    
    # Removed introductory markdown for compactness
    # st.markdown("""
    # **Compare AI model insights with actual data visualizations side-by-side**
    # 
    # This dashboard shows AI-generated insights alongside the corresponding charts and graphs for validation.
    # """)
    
    # Load data
    with st.spinner("Loading data and images..."):
        insights_data, airlines = load_insights_data()
        available_images = get_available_images()
    
    if not insights_data:
        # st.error("No insights data found. Please check the data directory structure.") # Removed for compactness
        return
    
    if not available_images:
        # st.error("No images found in cropped/ directory.") # Removed for compactness
        return
    
    # Find common airlines between insights and images
    common_airlines = set(airlines) & set(available_images.keys())
    if not common_airlines:
        # st.error("No common airlines found between insights and images.") # Removed for compactness
        return
    
    # Sidebar
    # st.sidebar.title("Controls") # Removed sidebar title for compactness
    
    # Airline selection (only show airlines with both data and images)
    selected_airline = st.sidebar.selectbox(
        "Select Airline",
        sorted(list(common_airlines)),
        # help="Airlines with both AI insights and visualizations" # Removed help text
    )
    
    # Show available channels for selected airline
    # Removed for compactness
    # if selected_airline and selected_airline in available_images:
    #     available_channels = list(available_images[selected_airline].keys())
    #     st.sidebar.markdown(f"**Available channels for {selected_airline}:** {', '.join(available_channels)}")
    
    # Section selection - filter by available images
    all_sections = [
        ("ota_highlights", "OTA Highlights"),
        ("ota_summary_high_level_comparison", "OTA High-Level Comparison"),
        ("ota_summary_by_region", "OTA by Region"),
        ("ota_summary_by_point_of_origin", "OTA by Origin"),
        ("ota_summary_by_booking_window", "OTA by Booking Window"),
        ("mse_highlights", "MSE Highlights"),
        ("mse_summary_high_level_comparison", "MSE High-Level Comparison"),
        ("mse_summary_by_region", "MSE by Region"),
        ("mse_summary_by_point_of_origin", "MSE by Origin"),
        ("mse_summary_by_booking_window", "MSE by Booking Window"),
        ("gds_highlights", "GDS Highlights"),
        ("gds_summary_high_level_comparison", "GDS High-Level Comparison"),
        ("gds_summary_by_region", "GDS by Region"),
        ("gds_summary_by_point_of_origin", "GDS by Origin"),
        ("gds_summary_by_booking_window", "GDS by Booking Window")
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
        # st.warning("No matching sections found for selected airline.") # Removed for compactness
        return
    
    selected_section = st.sidebar.selectbox(
        "Select Analysis Section",
        [s[0] for s in available_sections],
        format_func=lambda x: next(s[1] for s in available_sections if s[0] == x),
        # help="Sections with both AI insights and visualizations" # Removed help text
    )
    
    # Model selection
    available_models = list(insights_data.keys())
    selected_models = st.sidebar.multiselect(
        "Select AI Models",
        available_models,
        default=available_models,
        # help="Select one or more AI models to compare their insights" # Removed help text
    )
    
    if not selected_airline or not selected_section or not selected_models:
        # st.warning("Please select an Airline, Analysis Section, and at least one AI Model.") # Removed for compactness
        return
    
    # Main content
    section_title = next(s[1] for s in available_sections if s[0] == selected_section)
    
    # Display insights with image
    display_insights_with_image(
        {model: insights_data[model][selected_airline] for model in selected_models},
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