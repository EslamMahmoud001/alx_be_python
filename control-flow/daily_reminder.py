# This script will ask the user for a single task, its priority level, and if it is time-sensitive. 
# demonstrating control flow and loops without relying on data structures to store multiple tasks.
# The program will then provide a customized reminder for that task, 

task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()

match priority:
    case 'high':
        reminder_text = f"{task} is a high priority task"
    case 'medium':
        reminder_text = f"{task} is a medium priority task"
    case 'low':
        reminder_text = f"{task} is a low priority task"
    case _: 
        reminder_text = f"{task} is a - priority task"
    
if time_bound == 'yes':
    reminder = f"{reminder_text} that requires immediate attention today!"
else:
    reminder = f"{reminder_text}. Consider completing it when you have free time."
    
print(f"Reminder: {reminder}")
    
    