# 🚀 Quick Start Guide

## Immediate Use - Single Dashboard

**Compare AI insights with actual data visualizations:**

1. **Install and run**: 
   ```bash
   pip install -r requirements.txt
   streamlit run dashboard.py
   ```

2. **Select an airline**: Choose from airlines that have both AI insights and images
3. **Pick a section**: Select analysis type (OTA, MSE, GDS) and breakdown (all, region, etc.)
4. **Compare**: View chart on left, AI insights on right

✅ **Visual validation** - See if AI insights match the actual charts  
✅ **Perfect integration** - Images automatically matched to insights  
✅ **Clean interface** - Only one file to run  

---

## What You'll See

### 📊 Left Side: Data Visualizations
- **Cropped charts** from `cropped/` directory
- **Actual data** showing pricing patterns
- **Professional graphs** with clear metrics

### 🤖 Right Side: AI Insights  
- **5 AI Models**: GPT-4o, GPT-4o-mini, O1, O3, O3-mini
- **Color-coded** for easy identification
- **Real analysis** of the same data shown in charts

---

## File Structure (Simple!)

```
pdf-compare/
├── dashboard.py          # ← Only file you need to run
├── requirements.txt      # Dependencies  
├── README.md            # Full documentation
├── QUICK_START.md       # This guide
├── cropped/             # Chart images (provided)
└── specified_models_run_*/ # AI insights (provided)
```

**No confusion - just one dashboard file!**

---

## Available Airlines & Analysis

### 🛫 Airlines Available
Airlines with both insights and visualizations:
- **UA** (United Airlines)
- **UX** (Air Europa)  
- **VA** (Virgin Australia)
- **VN** (Vietnam Airlines)
- **VS** (Virgin Atlantic)
- **VY** (Vueling)
- **WF** (Wideroe)
- **WS** (WestJet)
- **WY** (Oman Air)

### 📊 Analysis Types
For each airline, compare across:
- **📊 High-Level** - Overall channel comparison
- **🌍 By Region** - Geographic breakdowns
- **📍 By Origin** - Point of origin analysis  
- **⏰ By Booking Window** - Time-based patterns

### 🔍 Channels
- **🌐 OTA** - Online Travel Agencies (Expedia, etc.)
- **🔍 MSE** - Meta Search Engines (Google Flights, etc.)
- **💼 GDS** - Global Distribution Systems (Amadeus, etc.)

---

## How to Use

### 🎯 Step-by-Step
1. **Run dashboard**: `streamlit run dashboard.py`
2. **Select airline**: Pick from dropdown (only shows airlines with data)
3. **Choose section**: Select channel and analysis type
4. **Compare**: Look at chart (left) vs AI insights (right)

### 🔍 What to Look For
- **✅ Accuracy**: Do AI insights match the chart?
- **📊 Numbers**: Are percentages consistent with visualization?
- **🤖 Consensus**: Do all AI models agree?
- **🎯 Differences**: Where do models disagree and why?

---

## Understanding the Interface

### 🎨 Model Colors
- 🔴 **GPT-4o** - Most advanced model
- 🟢 **GPT-4o-mini** - Efficient version
- 🔵 **O1** - Reasoning-focused  
- 🟢 **O3** - Latest generation
- 🟡 **O3-mini** - Compact latest

### 📋 Smart Filtering
- **Automatic matching** - Only shows combinations that exist
- **Available channels** - Shows what data exists for each airline
- **Error prevention** - Can't select invalid combinations

---

## Perfect For

### 📊 Data Scientists
- **Validate AI outputs** against actual data
- **Compare model performance** on same dataset
- **Find interpretation differences** between models

### ✈️ Airline Analysts
- **Cross-reference insights** with visual data
- **Spot inconsistencies** in AI analysis
- **Build confidence** in automated insights

### 🔬 Researchers  
- **Study AI accuracy** on real business data
- **Document model differences** across scenarios
- **Publish findings** on AI reliability

---

## Quick Troubleshooting

**No airlines showing?**
- Check both `cropped/` and `specified_models_run_*/` directories exist

**Images not loading?**  
- Verify PNG files are in `cropped/` directory
- Check filename format matches pattern

**Missing insights?**
- Confirm JSON files exist for selected airline
- Verify file structure is correct

---

## Next Steps

1. **Start with UA** - Good example airline with complete data
2. **Try different sections** - See how models handle various analysis types  
3. **Compare channels** - Notice differences between OTA/MSE/GDS insights
4. **Look for patterns** - Which models are most accurate? Most consistent?
5. **Share findings** - Dashboard URL can be shared with team

---

**🎉 Ready to validate AI insights against real data!**  
**Run `streamlit run dashboard.py` and start exploring.** 