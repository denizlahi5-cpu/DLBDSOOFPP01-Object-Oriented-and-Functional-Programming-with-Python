"""Visual analytics for habit tracking using matplotlib."""

import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta
from analytics import list_all_habits, filter_by_periodicity, get_longest_streak, get_streak_for_habit

# Create visualizations directory if it doesn't exist
VIZ_DIR = "visualizations"
os.makedirs(VIZ_DIR, exist_ok=True)


def plot_completion_rates(manager):
    """Bar chart showing completion rates for all habits."""
    habits = manager.habits
    names = [h.name for h in habits]
    completion_counts = [len(h.completions) for h in habits]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, completion_counts, color=['#2ecc71', '#3498db', '#9b59b6', '#f39c12', '#e74c3c'])
    
    plt.title('Habit Completion Counts (Last 4 Weeks)', fontsize=16, fontweight='bold')
    plt.xlabel('Habits', fontsize=12)
    plt.ylabel('Number of Completions', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    filepath = os.path.join(VIZ_DIR, 'completion_rates.png')
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {filepath}")
    plt.show()


def plot_streaks_comparison(manager):
    """Bar chart comparing streaks across habits."""
    habits = manager.habits
    names = [h.name for h in habits]
    streaks = [h.calculate_streak() for h in habits]
    
    plt.figure(figsize=(10, 6))
    colors = ['#e74c3c' if s == max(streaks) else '#3498db' for s in streaks]
    bars = plt.bar(names, streaks, color=colors)
    
    plt.title('Habit Streaks Comparison', fontsize=16, fontweight='bold')
    plt.xlabel('Habits', fontsize=12)
    plt.ylabel('Consecutive Periods', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    filepath = os.path.join(VIZ_DIR, 'streaks_comparison.png')
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {filepath}")
    plt.show()


def plot_daily_vs_weekly(manager):
    """Pie chart showing distribution of daily vs weekly habits."""
    daily = len(filter_by_periodicity(manager.habits, 'daily'))
    weekly = len(filter_by_periodicity(manager.habits, 'weekly'))
    
    plt.figure(figsize=(8, 8))
    sizes = [daily, weekly]
    labels = [f'Daily ({daily})', f'Weekly ({weekly})']
    colors = ['#3498db', '#e74c3c']
    explode = (0.05, 0.05)
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            textprops={'fontsize': 14, 'fontweight': 'bold'})
    
    plt.title('Habit Distribution by Periodicity', fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    
    filepath = os.path.join(VIZ_DIR, 'periodicity_distribution.png')
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {filepath}")
    plt.show()


def plot_completion_timeline(manager, habit_name):
    """Timeline showing when a specific habit was completed."""
    habit = None
    for h in manager.habits:
        if h.name == habit_name:
            habit = h
            break
    
    if not habit:
        print(f"Error: Habit '{habit_name}' not found")
        return
    
    if not habit.completions:
        print(f"No completions recorded for '{habit_name}'")
        return
    
    # Parse completion dates
    dates = [datetime.fromisoformat(c) for c in habit.completions]
    
    # Create timeline
    plt.figure(figsize=(14, 6))
    
    # Plot completions as vertical lines
    for date in dates:
        plt.axvline(x=date, color="#c9cc2e", alpha=0.6, linewidth=2)
    
    # Plot markers
    y_vals = [1] * len(dates)
    plt.scatter(dates, y_vals, s=100, color='#27ae60', zorder=5, edgecolors='white', linewidths=2)
    
    plt.title(f'Completion Timeline: {habit_name}', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('')
    plt.yticks([])
    plt.grid(axis='x', alpha=0.3)
    plt.gcf().autofmt_xdate()
    
    plt.tight_layout()
    filename = f'timeline_{habit_name.replace(" ", "_")}.png'
    filepath = os.path.join(VIZ_DIR, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {filepath}")
    plt.show()


def plot_weekly_heatmap(manager, habit_name):
    """Heatmap showing completion pattern over the last 4 weeks."""
    habit = None
    for h in manager.habits:
        if h.name == habit_name:
            habit = h
            break
    
    if not habit:
        print(f"Error: Habit '{habit_name}' not found")
        return
    
    # Create 4x7 grid for 4 weeks
    start_date = datetime.fromisoformat(habit.created_date)
    completion_dates = [datetime.fromisoformat(c).date() for c in habit.completions]
    
    data = []
    for week in range(4):
        week_data = []
        for day in range(7):
            date = (start_date + timedelta(weeks=week, days=day)).date()
            week_data.append(1 if date in completion_dates else 0)
        data.append(week_data)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(data, cmap='Greens', aspect='auto', vmin=0, vmax=1)
    
    plt.title(f'Completion Heatmap: {habit_name}', fontsize=16, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Week', fontsize=12)
    plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.yticks(range(4), [f'Week {i+1}' for i in range(4)])
    
    # Add completion markers
    for i in range(4):
        for j in range(7):
            text = plt.text(j, i, '✓' if data[i][j] else '',
                          ha="center", va="center", color="white", fontsize=16, fontweight='bold')
    
    plt.colorbar(label='Completed', ticks=[0, 1])
    plt.tight_layout()
    filename = f'heatmap_{habit_name.replace(" ", "_")}.png'
    filepath = os.path.join(VIZ_DIR, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {filepath}")
    plt.show()


def generate_all_visualizations(manager):
    """Generate all available visualizations."""
    print("\n" + "="*70)
    print("GENERATING VISUAL ANALYTICS")
    print("="*70)
    
    print("\n Creating visualizations...")
    
    # Overview charts
    plot_completion_rates(manager)
    plot_streaks_comparison(manager)
    plot_daily_vs_weekly(manager)
    
    # Individual habit charts
    for habit in manager.habits:
        plot_completion_timeline(manager, habit.name)
        plot_weekly_heatmap(manager, habit.name)
    
    print("\n" + "="*70)
    print(f" Generated {3 + len(manager.habits) * 2} visualizations!")
    print("="*70)
    print(f"\nFiles saved in '{VIZ_DIR}' folder:")
    print("  • completion_rates.png")
    print("  • streaks_comparison.png")
    print("  • periodicity_distribution.png")
    for habit in manager.habits:
        name = habit.name.replace(' ', '_')
        print(f"  • timeline_{name}.png")
        print(f"  • heatmap_{name}.png")


if __name__ == "__main__":
    from habit_manager import HabitManager
    
    manager = HabitManager()
    generate_all_visualizations(manager)
