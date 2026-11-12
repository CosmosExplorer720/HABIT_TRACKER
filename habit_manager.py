import pandas as pd
from model import Habit, Player

class HabitManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.habits = {}
        self.player = Player()
        
    def load_data(self):
        self.df = pd.read_csv(self.file_path)

        self.df = self.df.sort_values("date").drop_duplicates(
            subset=["date", "habit_name"], keep="last"
        )
        
    def process_habits(self):
        for row in self.df.itertuples(index=False):
            name = row.habit_name
            completed = row.completed

            if name not in self.habits:
                self.habits[name] = Habit(name)

            habit = self.habits[name]
            habit.update_streak(completed)

            if completed:
                xp = habit.gain_xp()
                # to add continuous xp for the player for each of his habit unless the streak is non zero
                if habit.streak % 7 == 0 and habit.streak != 0:
                    xp += 20

                habit.xp += xp
                self.player.add_xp(xp)
    
    def generate_report(self):
        report = []

        for habit in self.habits.values():
            report.append({
                "habit": habit.name,
                "streak": habit.streak,
                "xp": habit.xp,
                "title": habit.get_streak_title(),
                "status": habit.get_status_message()
            })

        # Sort of streak
        # here I'm using lamnda to make a oneline unnamed function
        report.sort(key=lambda x: x["streak"], reverse=True) #this will convert the strak in descending order

        return report