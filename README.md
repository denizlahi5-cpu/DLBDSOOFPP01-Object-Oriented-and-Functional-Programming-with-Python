# DLBDSOOFPP01-Object-Oriented-and-Functional-Programming-with-Python

# Habit Tracking App

A comprehensive Python-based habit tracking application to help you build and maintain positive habits with analytics and visual insights.

## Features

- **Track Multiple Habits**: Manage both daily and weekly habits
- **Smart Completion Tracking**: Mark habits as complete with automatic timestamping
- **Advanced Streak Calculations**: Monitor consistency with intelligent streak algorithms
- **Comprehensive Analytics**: View completion rates, streaks, and performance insights
- **Visual Analytics**: Generate beautiful charts and visualizations (matplotlib)
- **Data Persistence**: Automatic JSON-based storage
- **Predefined Habits**: Start with 5 example habits and 4 weeks of sample data

## Project Structure


habit_tracker/
•	habit.py              # Habit class with streak calculation
•	habit_manager.py      # Manages multiple habits and persistence
•	analytics.py          # Pure analytics functions
•	visualize.py          # Visual analytics with matplotlib
•	main.py              # CLI application entry point
•	test_phase1.py       # Phase 1 functionality tests
•	test_app.py          # Comprehensive integration tests
•	.gitignore           # Git ignore rules
•	habits.json          # Persistent data storage (auto-generated)
•	tests/               # Test directory
•	test_unit.py     # Comprehensive unit tests (25 tests)
•	test_data_*.json # Sample test data (4 weeks)
•	README.md        # Test data documentation
•	visualizations/      # Generated charts and graphs
•	*.png            # Visualization outputs



## Code Quality

### Design Principles

**Modular Architecture**: Clean separation of concerns
- `Habit` class: Core habit logic and streak calculations
- `HabitManager`: Persistence and CRUD operations  
- `analytics.py`: Pure functions for data analysis
- `visualize.py`: Visual analytics generation

**Python Naming Conventions**:
- Classes: `PascalCase` (Habit, HabitManager)
- Functions: `snake_case` (calculate_streak, list_all_habits)
- Variables: `snake_case` (periodicity, completion_time)

**Best Practices**:
- Type hints for clarity
- Comprehensive docstrings
- Error handling with meaningful exceptions
- JSON serialization/deserialization
- ISO format timestamps

## Installation

No external dependencies required for core functionality! 

For visual analytics (optional):
```bash
pip install matplotlib
```

## Usage

### Basic CLI Interface

```bash
python main.py
```

Menu options:
1. List all habits (alphabetically sorted)
2. List habits by periodicity (daily/weekly)
3. Create new habit
4. Delete habit
5. Check off habit (mark complete)
6. Get longest streak across all habits
7. Get streak for specific habit
8. Generate visual analytics
9. Exit

### Quick Start Example

```python
from habit_manager import HabitManager
from analytics import list_all_habits, get_longest_streak

# Initialize manager (loads predefined habits)
manager = HabitManager()

# List all habits
habits = list_all_habits(manager.habits)
print(f"Your habits: {habits}")

# Create new habit
manager.create_habit("Morning Yoga", "daily")

# Mark habit complete
manager.check_off("Morning Yoga")

# Get analytics
longest = get_longest_streak(manager.habits)
print(f"Longest streak: {longest} periods")
```

## Analytics Functions

### Core Analytics (`analytics.py`)

- **`list_all_habits(habits)`**: Returns alphabetically sorted list of habit names
- **`filter_by_periodicity(habits, periodicity)`**: Filter habits by 'daily' or 'weekly'
- **`get_longest_streak(habits)`**: Returns longest streak across all habits
- **`get_streak_for_habit(habits, name)`**: Returns streak for specific habit

### Streak Calculation Algorithm

The streak calculation algorithm works for both daily and weekly habits:

1. **Daily Habits**: Counts consecutive days with at least one completion
2. **Weekly Habits**: Counts consecutive weeks with at least one completion
3. **Smart Gap Detection**: Automatically resets streak on missed periods
4. **Historical Tracking**: Calculates from habit creation date to present

Example:
- Created: Jan 6, 2025
- Completions: Jan 6, 7, 8, [skip 9], 10, 11...
- Result: Max streak = 3 (first 3 consecutive days)

## Testing

### Test Suite Overview

âœ… **3 Test Suites - 45 Total Tests**

1. **Phase 1 Tests** (`test_phase1.py`): 10 integration tests
2. **Comprehensive Tests** (`test_app.py`): 10 end-to-end tests  
3. **Unit Tests** (`tests/test_unit.py`): 25 unit tests

### Test Coverage

**Habit Class**:
-Creation and initialization
-Mark complete (with/without custom time)
-Streak calculation (daily/weekly, empty, with gaps)
-Serialization (to_dict/from_dict)

**HabitManager Class**:
- Initialization with predefined habits
- Create habit (including duplicate prevention)
- Delete habit
- Check off habit
- Data persistence (save/load JSON)

**Analytics Functions**:
- List all habits (alphabetical sorting)
- Filter by periodicity
- Get longest streak (including empty list)
- Get streak for habit (including error handling)

**Edge Cases**:
- Future creation dates
- Old creation dates (365+ days)
- Multiple completions same day
- Error handling (non-existent habits, duplicates)

### Running Tests

```bash
# Phase 1 functionality tests
python test_phase1.py

# Comprehensive integration tests
python test_app.py

# Full unit test suite
python tests/test_unit.py

# All tests with summary
python capture_test_results.py
```

### Test Results

**Latest Test Run: February 3, 2026**

```
======================================================================
PHASE 1 TESTS
======================================================================
[PASS] 5 predefined habits loaded
[PASS] Correct periodicity filtering  
[PASS] Streak calculation working
[PASS] Individual habit streak calculation working
[PASS] Habit creation working
[PASS] Check-off functionality working
[PASS] Habit deletion working
[PASS] Data persisted to JSON file
[PASS] Data successfully loaded from JSON

ALL PHASE 1 TESTS PASSED! [SUCCESS]

======================================================================
COMPREHENSIVE TESTS
======================================================================
[PASS] Initialization
[PASS] List all habits
[PASS] Filter by periodicity
[PASS] Streak calculations
[PASS] Create new habit
[PASS] Check off habit
[PASS] Delete habit
[PASS] Data persistence
[PASS] Error handling
[PASS] Completion data

All 10 tests PASSED successfully! [SUCCESS]

======================================================================
UNIT TESTS
======================================================================
Ran 25 tests in 0.054s - OK

Tests run: 25
Successes: 25
Failures: 0
Errors: 0

[SUCCESS] ALL TESTS PASSED!
======================================================================
```

## Test Data

The `tests/` directory contains 4 weeks of sample habit tracking data:

- **test_data_daily_workout.json**: Daily habit with ~21 completions
- **test_data_weekly_review.json**: Weekly habit with 4 completions
- Data spans: January 6, 2025 - February 3, 2025

## Predefined Habits

The application initializes with 5 example habits and 4 weeks of data:

**Daily Habits** (3):
- Drink water
- Study Python  
- Walk 10k Steps

**Weekly Habits** (2):
- Clean Apartment
- Do Laundry

Each has realistic completion patterns with ~19 completions showing consistency with occasional breaks.

## Visual Analytics

Generate charts and visualizations:

```bash
python main.py
# Choose option 8: Generate visual analytics
```

**Available Visualizations**:
1. Completion rates bar chart
2. Streak comparison chart
3. Daily vs weekly distribution pie chart
4. Completion timeline
5. Weekly heatmap

All visualizations saved to `visualizations/` directory as high-resolution PNG files (300 DPI).

## Data Persistence

- **Format**: JSON
- **File**: `habits.json`
- **Auto-save**: After every create/delete/check-off operation
- **Auto-load**: On HabitManager initialization

Example data structure:
```json
{
  "name": "Drink water",
  "periodicity": "daily",
  "created_date": "2025-01-06T08:00:00",
  "completions": [
    "2025-01-06T08:30:00",
    "2025-01-07T08:15:00"
  ]
}
```

## API Documentation

### Habit Class

```python
class Habit:
    def __init__(name, periodicity, created_date=None, completions=None)
    def mark_complete(completion_time=None)
    def calculate_streak() -> int
    def to_dict() -> dict
    @classmethod from_dict(data) -> Habit
```

### HabitManager Class

```python
class HabitManager:
    def __init__(file_path='habits.json')
    def create_habit(name, periodicity)
    def delete_habit(name)
    def check_off(name, completion_time=None)
    def save_habits()
    def load_habits() -> list[Habit]
```

### Analytics Functions

```python
def list_all_habits(habits: list[Habit]) -> list[str]
def filter_by_periodicity(habits: list[Habit], periodicity: str) -> list[str]
def get_longest_streak(habits: list[Habit]) -> int
def get_streak_for_habit(habits: list[Habit], name: str) -> int
```

## Development

### Git Setup

A `.gitignore` file is included to exclude:
- `__pycache__/` and `*.pyc` files
- `habits.json` (user data)
- Virtual environments
- IDE settings
- Log files

### Project Standards

- Python 3.12+
- No required dependencies (core functionality)
- Optional: matplotlib for visualizations
- Follows PEP 8 style guidelines
- Type hints for clarity
- Comprehensive docstrings

## Future Enhancements

Potential improvements:
- [ ] Database backend (SQLite)
- [ ] Web interface (Flask/Django)
- [ ] Mobile app integration
- [ ] Reminders and notifications
- [ ] Habit categories and tags
- [ ] Social features (share progress)
- [ ] Export to CSV/Excel
- [ ] Advanced statistics (trends, predictions)

## License

MIT License - feel free to use and modify as needed!

## Contributing

Contributions welcome! Please ensure:
1. All tests pass (`python tests/test_unit.py`)
2. Code follows Python naming conventions
3. New features include tests
4. Documentation is updated

