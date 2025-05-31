task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()


match priority:
    case "high":
        message = f"Reminder:'{task}' is a high priority task "
    case "medium":
        message = f"Reminder:'{task}' is a medium priority task "
    case "low":
        message = f"Reminder:'{task}' is a low priority task "
    case _:
        message = f"Reminder:'{task}' is a unknown priority task "



if time_bound == "yes" and priority in ("high", "medium", "low"):
    message += "that requires immediate attention today!"

elif priority in ("low", "medium") and time_bound == "no":
    message += ". Consider completing it when you have free time."



print("\n" + message)



