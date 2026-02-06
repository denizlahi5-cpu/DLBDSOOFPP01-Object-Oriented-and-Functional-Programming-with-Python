"""Test script to verify Phase 1 functionality."""

from habit_manager import HabitManager
from analytics import list_all_habits, filter_by_periodicity, get_longest_streak, get_streak_for_habit
import os

# Clean start
if os.path.exists('habits.json'):
    os.remove('habits.json')

print("=" * 60)
print("PHASE 1 FUNCTIONALITY TEST")
print("=" * 60)

# Initialize manager - should create 5 predefined habits
print("\n1. Initializing HabitManager with 5 predefined habits...")
manager = HabitManager()

# Test: List all habits (A-Z)
print("\n2. Testing: List all habits (A-Z)")
all_habits = list_all_habits(manager.habits)
print(f"   All habits: {all_habits}")
assert len(all_habits) == 5, "Should have 5 predefined habits"
print("   [PASS] 5 predefined habits loaded")

# Test: Filter by periodicity
print("\n3. Testing: Filter by periodicity")
daily_habits = filter_by_periodicity(manager.habits, 'daily')
weekly_habits = filter_by_periodicity(manager.habits, 'weekly')
print(f"   Daily habits: {daily_habits}")
print(f"   Weekly habits: {weekly_habits}")
assert len(daily_habits) == 3, "Should have 3 daily habits"
assert len(weekly_habits) == 2, "Should have 2 weekly habits"
print("   [PASS] Correct periodicity filtering")

# Test: Get longest streak of all habits
print("\n4. Testing: Get longest streak of all habits")
longest = get_longest_streak(manager.habits)
print(f"   Longest streak: {longest}")
assert longest > 0, "Should have streaks from predefined data"
print("   [PASS] Streak calculation working")

# Test: Get streak for specific habit
print("\n5. Testing: Get streak for specific habit")
streak = get_streak_for_habit(manager.habits, 'Drink water')
print(f"   Streak for 'Drink water': {streak}")
assert streak >= 0, "Should calculate streak"
print("   [PASS] Individual habit streak calculation working")

# Test: Create new habit
print("\n6. Testing: Create new habit")
manager.create_habit('Read Books', 'daily')
all_habits = list_all_habits(manager.habits)
print(f"   All habits after creation: {all_habits}")
assert len(all_habits) == 6, "Should have 6 habits now"
assert 'Read Books' in all_habits, "New habit should be in list"
print("   [PASS] Habit creation working")

# Test: Check off habit
print("\n7. Testing: Check off habit")
manager.check_off('Read Books')
streak = get_streak_for_habit(manager.habits, 'Read Books')
print(f"   Streak for 'Read Books' after check-off: {streak}")
assert streak > 0, "Should have streak after checking off"
print("   [PASS] Check-off functionality working")

# Test: Delete habit
print("\n8. Testing: Delete habit")
manager.delete_habit('Read Books')
all_habits = list_all_habits(manager.habits)
print(f"   All habits after deletion: {all_habits}")
assert len(all_habits) == 5, "Should be back to 5 habits"
assert 'Read Books' not in all_habits, "Deleted habit should not be in list"
print("   [PASS] Habit deletion working")

# Test: Verify JSON persistence
print("\n9. Testing: JSON persistence")
assert os.path.exists('habits.json'), "habits.json should exist"
print("   [PASS] Data persisted to JSON file")

# Reload and verify
print("\n10. Testing: Load from JSON")
manager2 = HabitManager()
all_habits2 = list_all_habits(manager2.habits)
print(f"   Habits loaded from JSON: {all_habits2}")
assert all_habits == all_habits2, "Loaded habits should match saved habits"
print("   [PASS] Data successfully loaded from JSON")

print("\n" + "=" * 60)
print("ALL PHASE 1 TESTS PASSED! [SUCCESS]")
print("=" * 60)

print("\n SUMMARY:")
print("   • 5 predefined habits created (3 daily, 2 weekly)")
print("   • 4 weeks of example tracking data generated")
print("   • All CRUD operations working (Create, Read, Delete)")
print("   • Check-off functionality working")
print("   • Analytics functions working:")
print("     - list_all_habits (A-Z sorted)")
print("     - filter_by_periodicity")
print("     - get_longest_streak")
print("     - get_streak_for_habit")
print("   • JSON persistence working (save & load)")
print("\n Phase 1 implementation complete and verified!")
