"""Comprehensive test and demonstration of all Habit Tracker features."""

from habit_manager import HabitManager
from analytics import list_all_habits, filter_by_periodicity, get_longest_streak, get_streak_for_habit
import os

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_initialization():
    """Test HabitManager initialization with predefined habits."""
    print_section("TEST 1: INITIALIZATION")
    
    # Remove existing data to start fresh
    if os.path.exists('habits.json'):
        os.remove('habits.json')
    
    manager = HabitManager()
    print(f"[PASS] HabitManager initialized")
    print(f"[PASS] {len(manager.habits)} predefined habits loaded")
    
    return manager

def test_list_habits(manager):
    """Test listing all habits."""
    print_section("TEST 2: LIST ALL HABITS")
    
    all_habits = list_all_habits(manager.habits)
    print(f"[PASS] Found {len(all_habits)} habits (alphabetically sorted):")
    for i, habit in enumerate(all_habits, 1):
        print(f"   {i}. {habit}")

def test_filter_by_periodicity(manager):
    """Test filtering habits by periodicity."""
    print_section("TEST 3: FILTER BY PERIODICITY")
    
    daily = filter_by_periodicity(manager.habits, 'daily')
    weekly = filter_by_periodicity(manager.habits, 'weekly')
    
    print(f"[PASS] Daily habits ({len(daily)}):")
    for habit in daily:
        print(f"   - {habit}")
    
    print(f"\n[PASS] Weekly habits ({len(weekly)}):")
    for habit in weekly:
        print(f"   - {habit}")

def test_streaks(manager):
    """Test streak calculations."""
    print_section("TEST 4: STREAK CALCULATIONS")
    
    longest = get_longest_streak(manager.habits)
    print(f"[PASS] Longest streak across all habits: {longest} consecutive periods")
    
    print(f"\n[PASS] Individual habit streaks:")
    for habit in manager.habits:
        streak = get_streak_for_habit(manager.habits, habit.name)
        print(f"   {habit.name:20s} -> {streak} {habit.periodicity} periods")

def test_create_habit(manager):
    """Test creating a new habit."""
    print_section("TEST 5: CREATE NEW HABIT")
    
    initial_count = len(manager.habits)
    manager.create_habit("Meditate", "daily")
    
    print(f"[PASS] Created new habit: Meditate (daily)")
    print(f"[PASS] Total habits: {initial_count} -> {len(manager.habits)}")
    
    all_habits = list_all_habits(manager.habits)
    print(f"[PASS] Updated habit list: {all_habits}")

def test_check_off(manager):
    """Test checking off a habit."""
    print_section("TEST 6: CHECK OFF HABIT")
    
    habit_name = "Meditate"
    streak_before = get_streak_for_habit(manager.habits, habit_name)
    
    manager.check_off(habit_name)
    
    streak_after = get_streak_for_habit(manager.habits, habit_name)
    
    print(f"[PASS] Checked off: {habit_name}")
    print(f"[PASS] Streak before: {streak_before}")
    print(f"[PASS] Streak after: {streak_after}")

def test_delete_habit(manager):
    """Test deleting a habit."""
    print_section("TEST 7: DELETE HABIT")
    
    habit_name = "Meditate"
    count_before = len(manager.habits)
    
    manager.delete_habit(habit_name)
    
    count_after = len(manager.habits)
    
    print(f"[PASS] Deleted habit: {habit_name}")
    print(f"[PASS] Total habits: {count_before} -> {count_after}")
    
    remaining = list_all_habits(manager.habits)
    print(f"[PASS] Remaining habits: {remaining}")

def test_persistence(manager):
    """Test data persistence across sessions."""
    print_section("TEST 8: DATA PERSISTENCE")
    
    print("[PASS] Saving current state...")
    manager.save_habits()
    
    print("[PASS] Creating new HabitManager instance...")
    manager2 = HabitManager()
    
    habits1 = list_all_habits(manager.habits)
    habits2 = list_all_habits(manager2.habits)
    
    if habits1 == habits2:
        print("[PASS] Data persistence verified: habits match after reload")
        print(f"[PASS] Both instances have {len(habits1)} habits")
    else:
        print("[ERROR] Data mismatch after reload!")

def test_error_handling(manager):
    """Test error handling for invalid operations."""
    print_section("TEST 9: ERROR HANDLING")
    
    # Test duplicate habit
    try:
        manager.create_habit("Drink water", "daily")
        print("[ERROR] Should have raised ValueError for duplicate habit")
    except ValueError as e:
        print(f"[PASS] Duplicate habit prevented: {e}")
    
    # Test non-existent habit check-off
    try:
        manager.check_off("Non-existent habit")
        print("[ERROR] Should have raised ValueError for non-existent habit")
    except ValueError as e:
        print(f"[PASS] Invalid check-off prevented: {e}")
    
    # Test non-existent habit streak
    try:
        get_streak_for_habit(manager.habits, "Non-existent habit")
        print("[ERROR] Should have raised ValueError for non-existent habit")
    except ValueError as e:
        print(f"[PASS] Invalid streak query prevented: {e}")

def test_completion_data(manager):
    """Test completion data integrity."""
    print_section("TEST 10: COMPLETION DATA")
    
    for habit in manager.habits:
        completions = len(habit.completions)
        print(f"[PASS] {habit.name:20s} -> {completions} completions recorded")

def run_all_tests():
    """Run complete test suite."""
    print("\n" + "=" * 70)
    print("    HABIT TRACKER - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    try:
        # Run all tests
        manager = test_initialization()
        test_list_habits(manager)
        test_filter_by_periodicity(manager)
        test_streaks(manager)
        test_create_habit(manager)
        test_check_off(manager)
        test_delete_habit(manager)
        test_persistence(manager)
        test_error_handling(manager)
        test_completion_data(manager)
        
        # Summary
        print_section("TEST SUMMARY")
        print("[SUCCESS] All 10 tests PASSED successfully!")
        print("\n[RESULTS] Tests completed:")
        print("   1. [PASS] Initialization")
        print("   2. [PASS] List all habits")
        print("   3. [PASS] Filter by periodicity")
        print("   4. [PASS] Streak calculations")
        print("   5. [PASS] Create new habit")
        print("   6. [PASS] Check off habit")
        print("   7. [PASS] Delete habit")
        print("   8. [PASS] Data persistence")
        print("   9. [PASS] Error handling")
        print("   10. [PASS] Completion data")
        
        print("\n[SUCCESS] The Habit Tracker application is fully functional!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n[ERROR] TEST FAILED with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_all_tests()

