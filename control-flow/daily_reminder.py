task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:", task, "is a high priority task that requires immediate attention today!")
        else:
            print("Reminder:", task, "is a high priority task. Try to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print("Note:", task, "is a medium priority task with a deadline. Plan accordingly.")
        else:
            print("Note:", task, "is a medium priority task. Do it when possible.")
    case "low":
        if time_bound == "yes":
            print("Note:", task, "is a low priority task but time-bound. Don’t forget!")
        else:
            print("Note:", task, "is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Unknown priority level for task:", task)
