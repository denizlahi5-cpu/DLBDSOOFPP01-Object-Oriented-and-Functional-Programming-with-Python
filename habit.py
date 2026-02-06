from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, periodicity, created_date=None, completions=None):
        self.name = name
        self.periodicity = periodicity  # 'daily' or 'weekly'
        self.created_date = created_date or datetime.now().isoformat()
        self.completions = completions or []  # List of ISO strings

    def mark_complete(self, completion_time=None):
        """Mark the task as complete at the given time (default: now)."""
        time = completion_time or datetime.now()
        self.completions.append(time.isoformat())
        self.completions.sort()  # Keep sorted for streak calculation

    def calculate_streak(self):
        """Calculate the longest streak of consecutive periods with at least one completion."""
        if not self.completions:
            return 0

        # Parse dates
        created = datetime.fromisoformat(self.created_date)
        comp_dates = [datetime.fromisoformat(c) for c in self.completions]

        # Determine period delta
        if self.periodicity == 'daily':
            period_delta = timedelta(days=1)
        elif self.periodicity == 'weekly':
            period_delta = timedelta(weeks=1)
        else:
            raise ValueError("Invalid periodicity")

        # Find all periods from creation to now
        current_streak = 0
        max_streak = 0
        current_period_start = created

        while current_period_start < datetime.now():
            period_end = current_period_start + period_delta
            # Check if any completion in this period
            has_completion = any(current_period_start <= d < period_end for d in comp_dates)
            if has_completion:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0
            current_period_start = period_end

        return max_streak

    def to_dict(self):
        """Convert to dict for JSON serialization."""
        return {
            'name': self.name,
            'periodicity': self.periodicity,
            'created_date': self.created_date,
            'completions': self.completions
        }

    @classmethod
    def from_dict(cls, data):
        """Create from dict (for JSON deserialization)."""
        return cls(
            name=data['name'],
            periodicity=data['periodicity'],
            created_date=data['created_date'],
            completions=data['completions']
        )
