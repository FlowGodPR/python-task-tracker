# main.py - Personal Task Reward System
# Author: [Your Name]
# Date: [Today's Date]
# Description: A task tracker that helps users track their daily tasks, calculates progress, and provides motivational feedback.

# Get user information
user_name = input("Enter your name: ")

# Define tasks (modifiable)
tasks = {
    "Complete morning study session": 10,
    "Exercise for 30 minutes": 15,
    "Read a chapter of a book": 5
}

completed_tasks = 0
total_points = 0
total_tasks = len(tasks)

print("\nYour tasks for today:")
for i, task in enumerate(tasks.keys(), start=1):
    print(f"{i}. {task} ({tasks[task]} points)")

# Task completion loop
for task, points in tasks.items():
    while True:
        status = input(f"\nDid you complete '{task}'? (yes/no): ").strip().lower()
        if status in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if status == 'yes':
        completed_tasks += 1
        total_points += points

# Calculate progress
progress_percentage = (completed_tasks / total_tasks) * 100

# Provide feedback based on progress
print("\n--- Task Completion Summary ---")
print(f"Tasks completed: {completed_tasks}/{total_tasks}")
print(f"Total points earned: {total_points}")

if progress_percentage == 100:
    print(f"Amazing job, {user_name}! 🎉 You've completed all tasks and earned {total_points} points!")
elif progress_percentage >= 50:
    print(f"Great effort, {user_name}! You're more than halfway there. Keep going! 💪")
else:
    print(f"You're getting there, {user_name}! Every step counts. Don't give up! 🚀")

print("\nThank you for using the Task Tracker!")
