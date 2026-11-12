from habit_manager import HabitManager
from utility import save_report

def main():
    manager = HabitManager("data/habit.csv")
    
    manager.load_data()
    manager.process_habits()
    
    report = manager.generate_report()
    print("\n --- Habit Report ---\n")
    for r in report:
        print(f"{r['habit']} | Streak: {r['streak']} | XP: {r['xp']} | {r['title']} | {r['status']}")

    print("\n--- Player Stats ---\n")
    print(f"Level: {manager.player.level}")
    print(f"Total XP: {manager.player.total_xp}")
    print()
    
    save_report(report, "reports/habit_report.csv")

if __name__ == "__main__":
    main()