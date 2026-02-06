"""Main CLI application for the Habit Tracker."""

from habit_manager import HabitManager
from analytics import list_all_habits, filter_by_periodicity, get_longest_streak, get_streak_for_habit


def main():
    manager = HabitManager()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. List all habits")
        print("2. List habits by periodicity (daily/weekly)")
        print("3. Create habit")
        print("4. Delete habit")
        print("5. Check off habit")
        print("6. Get longest streak of all habits")
        print("7. Get streak for a habit")
        print("8. Generate visual analytics")
        print("9. Exit")

        choice = input("Enter choice: ").strip()

        try:
            if choice == '1':
                print("All habits:", list_all_habits(manager.habits))
            elif choice == '2':
                period = input("Enter periodicity (daily/weekly): ").strip()
                print(f"{period} habits:", filter_by_periodicity(manager.habits, period))
            elif choice == '3':
                name = input("Habit name: ").strip()
                period = input("Periodicity (daily/weekly): ").strip()
                manager.create_habit(name, period)
                print("Habit created.")
            elif choice == '4':
                name = input("Habit name to delete: ").strip()
                manager.delete_habit(name)
                print("Habit deleted.")
            elif choice == '5':
                name = input("Habit name to check off: ").strip()
                manager.check_off(name)
                print("Habit checked off.")
            elif choice == '6':
                print("Longest streak:", get_longest_streak(manager.habits))
            elif choice == '7':
                name = input("Habit name: ").strip()
                print("Streak:", get_streak_for_habit(manager.habits, name))
            elif choice == '8':
                try:
                    from visualize import generate_all_visualizations
                    generate_all_visualizations(manager)
                except ImportError:
                    print("Error: matplotlib not installed. Run: pip install matplotlib")
            elif choice == '9':
                break
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
