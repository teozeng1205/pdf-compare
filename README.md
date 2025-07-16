# ✈️ AI Models vs Data Visualizations Dashboard

Compare AI-generated insights with actual data visualizations side-by-side for airline pricing analysis.

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the dashboard:**
   ```bash
   streamlit run dashboard.py
   ```

3. **Open your browser** to `http://localhost:8501`

## 📊 What This Dashboard Does

**Side-by-side comparison** of:
- **Left side**: Actual data visualizations (cropped charts from `cropped/` directory)
- **Right side**: AI-generated insights from 5 different models analyzing the same data

This allows you to **validate AI insights** against the actual charts and graphs.

## 🎯 Features

### 📈 Visual Validation
- **Image integration**: Shows cropped charts alongside AI insights
- **Perfect matching**: AI insights are matched to corresponding visualizations
- **Multiple channels**: OTA, MSE, GDS analysis comparisons

### 🤖 AI Model Comparison  
- **5 AI Models**: GPT-4o, GPT-4o-mini, O1, O3, O3-mini
- **Color-coded**: Each model has distinct visual styling
- **Real insights**: Actual analysis from airline pricing data

### 📱 Smart Interface
- **Filtered selection**: Only shows airlines/sections with both data and images
- **Responsive design**: Works on desktop, tablet, mobile
- **Clean layout**: Focus on content comparison

## 📁 Data Structure

### Required Directories
```
pdf-compare/
├── dashboard.py                          # Main dashboard file
├── requirements.txt                      # Dependencies
├── cropped/                             # Data visualization images
│   ├── cropped_AA-OTA1-Compare_Live_Site_to_OTA-all.png
│   ├── cropped_AA-MSE2-Compare_Live_Site_to_MSE-region.png
│   └── ... (organized by airline-channel-type)
└── specified_models_run_20250715_230613/ # AI insights JSON files
    ├── insights_gpt-4o/
    ├── insights_gpt-4o-mini/
    ├── insights_o1/
    ├── insights_o3/
    └── insights_o3-mini/
```

### Image Naming Convention
Images follow this pattern: `cropped_{AIRLINE}-{CHANNEL}{NUMBER}-Compare_Live_Site_to_{CHANNEL}-{TYPE}.png`

Examples:
- `cropped_AA-OTA1-Compare_Live_Site_to_OTA-all.png`
- `cropped_UA-MSE2-Compare_Live_Site_to_MSE-region.png`
- `cropped_VS-GDS3-Compare_Live_Site_to_GDS-poo.png`

Where:
- **AIRLINE**: Two-letter airline code (AA, UA, VS, etc.)
- **CHANNEL**: OTA, MSE, or GDS
- **TYPE**: all, region, poo (point of origin), booking_window

## 🔍 Analysis Sections

### Available Comparisons
Each section shows AI insights alongside the corresponding chart:

- **📊 High-Level Comparison** - Overall channel analysis
- **🌍 By Region** - Geographic breakdowns  
- **📍 By Point of Origin** - Origin-based patterns
- **⏰ By Booking Window** - Time-based analysis

### Channels Analyzed
- **🌐 OTA** (Online Travel Agencies) - Expedia, Booking.com, etc.
- **🔍 MSE** (Meta Search Engines) - Google Flights, Kayak, etc.  
- **💼 GDS** (Global Distribution Systems) - Amadeus, Sabre, etc.

## 🎨 Model Color Coding

- 🔴 **GPT-4o** - Red gradient
- 🟢 **GPT-4o-mini** - Teal gradient
- 🔵 **O1** - Blue gradient  
- 🟢 **O3** - Green gradient
- 🟡 **O3-mini** - Yellow gradient

## 🛠️ Usage

### Basic Workflow
1. **Select an airline** (only airlines with both insights and images appear)
2. **Choose an analysis section** (filtered to available combinations)
3. **Pick AI models** to compare (all selected by default)
4. **Compare insights** with the visualization on the left

### Understanding Results
- **Look for consensus** - Do all AI models agree?
- **Check accuracy** - Do insights match what you see in the chart?
- **Note differences** - Where do models interpret data differently?
- **Validate claims** - Are percentage claims supported by the visualization?

## 📊 Available Airlines

Airlines with both insights and visualizations include:
UA, UX, VA, VN, VS, VY, WF, WS, WY (and more as data becomes available)

## 🔧 Troubleshooting

**"No common airlines found"**
- Ensure both `cropped/` images and `specified_models_run_*/` directories exist
- Check that airline codes match between JSON files and image filenames

**"No matching sections found"**  
- Verify image files follow the correct naming convention
- Check that the selected airline has images for the analysis type

**Images not displaying**
- Confirm image files are in PNG format
- Verify file paths are correct and accessible

**Missing AI insights**
- Check that JSON files exist for the selected models and airline
- Verify JSON structure contains the expected section keys

## 🔄 Adding New Data

### New Airlines
1. Add JSON files to each model directory following naming pattern: `{AIRLINE}_20250713_insights_{model}.json`
2. Add corresponding cropped images following the naming convention
3. Restart dashboard to see new options

### New Models  
1. Create new directory: `specified_models_run_*/insights_{model_name}/`
2. Add JSON files for each airline
3. Update `models` list in `dashboard.py`

## 📝 Technical Notes

- **Data caching**: Streamlit caches data loading for better performance
- **Image processing**: Images are displayed using Streamlit's native image handling
- **Path handling**: Uses pathlib for cross-platform compatibility
- **Error handling**: Gracefully handles missing files and invalid data

## 🎉 Perfect for

- **Data validation** - Verify AI accuracy against charts
- **Model comparison** - See how different AI models interpret the same data  
- **Insight discovery** - Find patterns across airlines and channels
- **Presentation** - Professional dashboard for sharing findings
- **Research** - Academic or business analysis of AI capabilities

---

**🚀 Start comparing AI insights with actual data visualizations!**
**Run `streamlit run dashboard.py` and explore the integrated analysis.** 