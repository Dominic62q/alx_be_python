task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match time_bound:
    case "yes":
        print("Reminder:", task, "is a high priority task that requires immediate attention today!")
    case "no":
        print("Note:", task, "is a low priority task. Consider completing it when you have free time.")    