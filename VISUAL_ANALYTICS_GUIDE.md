# Visual Analytics Guide

##  How to View Analytics Visualizations

Your habit tracker now includes powerful visual analytics! Here are the ways to access them:

---

## Method 1: From Main Application (Easiest)

1. **Run the main application:**
   ```bash
   python main.py
   ```

2. **Select option 8:**
   - The menu will show "8. Generate visual analytics"
   - Enter `8` and press Enter
   - All visualizations will be generated and displayed

3. **Exit:**
   - Enter `9` to exit

---

## Method 2: Generate All Visualizations Directly

**Run the visualization script:**
```bash
python visualize.py
```

This will:
- Generate 13 PNG image files in the current directory
- Display each visualization as it's created
- Save all images for later viewing

---

## Method 3: Interactive Viewer

**Run the viewer script:**
```bash
python view_analytics.py
```

This allows you to:
- Browse all generated visualizations
- View individual charts
- See all charts in a grid layout

---

##  Available Visualizations

### Overview Charts (3):

1. **completion_rates.png**
   - Bar chart showing total completions for each habit
   - Colored bars for easy comparison
   - Shows which habits you've been most consistent with

2. **streaks_comparison.png**
   - Bar chart comparing streaks across all habits
   - Highlights the habit with the longest streak
   - Shows your consistency patterns

3. **periodicity_distribution.png**
   - Pie chart showing daily vs weekly habit distribution
   - Percentages and counts included
   - Visual breakdown of habit types

### Individual Habit Charts (10):

For each of the 5 habits, you get:

4-8. **timeline_[HabitName].png**
   - Timeline showing when the habit was completed
   - Green markers for each completion
   - Easy to spot completion patterns

9-13. **heatmap_[HabitName].png**
   - 4-week heatmap with checkmarks
   - Shows completion pattern by day of week
   - Identifies your strong/weak days

---

##  Visualization Features

- **High Quality:** All images saved at 300 DPI
- **Color Coded:** Different colors for different habit types
- **Interactive:** Charts display in popup windows
- **Exportable:** PNG format, easy to share or print
- **Automated:** Updates with your latest habit data

---

##  Quick Commands

| Action | Command |
|--------|---------|
| Generate all charts | `python visualize.py` |
| View saved charts | `python view_analytics.py` |
| Run with menu | `python main.py` (option 8) |

---

##  File Locations

All visualization files are organized in a dedicated folder:

```
habit_tracker/
└── visualizations/
    ├── completion_rates.png
    ├── streaks_comparison.png
    ├── periodicity_distribution.png
    ├── timeline_Drink_water.png
    ├── heatmap_Drink_water.png
    ├── timeline_Study_Python.png
    ├── heatmap_Study_Python.png
    ├── timeline_Walk_10k_Steps.png
    ├── heatmap_Walk_10k_Steps.png
    ├── timeline_Clean_Apartment.png
    ├── heatmap_Clean_Apartment.png
    ├── timeline_Do_Laundry.png
    └── heatmap_Do_Laundry.png
```

**Full Path:**
```
d:\Areeb Data\areeb\Dec\16\Habit tracking app\habit_tracker\visualizations\
```

---

##  Requirements

- **Python 3.12+**
- **matplotlib** (already installed)
- **PIL/Pillow** (for viewer, optional)

If you need to install Pillow for the viewer:
```bash
pip install Pillow
```

---

##  Tips

1. **Regular Updates:** Run `python visualize.py` after checking off habits to see updated charts
2. **Track Progress:** Compare charts week-to-week to see improvements
3. **Identify Patterns:** Use heatmaps to find your best completion days
4. **Share Results:** PNG files are easy to share with accountability partners

---

Enjoy your visual analytics!
