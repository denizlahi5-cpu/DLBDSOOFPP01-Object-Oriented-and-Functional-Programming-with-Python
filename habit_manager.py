"""Habit Manager for managing multiple habits and persistence."""

import json
from datetime import datetime, timedelta
from habit import Habit


class HabitManager:
    def __init__(self, file_path='habits.json'):
        self.file_path = file_path
        self.habits = self.load_habits()

    def load_habits(self):
        """Load habits from JSON or initialize predefined with example data."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                return [Habit.from_dict(h) for h in data]
        except FileNotFoundError:
            # Initialize predefined habits with example data (4 weeks)
            start_date = datetime.now() - timedelta(weeks=4)
            predefined = [
                self._create_predefined('Drink water', 'daily', start_date),
                self._create_predefined('Study Python', 'daily', start_date),
                self._create_predefined('Walk 10k Steps', 'daily', start_date),
                self._create_predefined('Clean Apartment', 'weekly', start_date),
                self._create_predefined('Do Laundry', 'weekly', start_date)
            ]
            self.habits = predefined
            self.save_habits()
            return predefined

    def _create_predefined(self, name, periodicity, start_date):
        """Helper to create predefined habit with example completions over 4 weeks."""
        habit = Habit(name, periodicity, start_date.isoformat())
        # Add example completions: e.g., most days/weeks completed, some breaks
        for i in range(28):  # 4 weeks = 28 days
            if i % 3 != 2:  # Skip every 3rd for breaks (simulating data)
                comp_date = start_date + timedelta(days=i)
                habit.completions.append(comp_date.isoformat())
        habit.completions.sort()
        return habit

    def save_habits(self):
        """Save habits to JSON."""
        with open(self.file_path, 'w') as f:
            json.dump([h.to_dict() for h in self.habits], f, indent=4)

    def create_habit(self, name, periodicity):
        """Create a new habit."""
        if any(h.name == name for h in self.habits):
            raise ValueError("Habit already exists")
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.save_habits()

    def delete_habit(self, name):
        """Delete a habit by name."""
        self.habits = [h for h in self.habits if h.name != name]
        self.save_habits()

    def check_off(self, name, completion_time=None):
        """Check off a habit by name."""
        for habit in self.habits:
            if habit.name == name:
                habit.mark_complete(completion_time)
                self.save_habits()
                return
        raise ValueError("Habit not found")
