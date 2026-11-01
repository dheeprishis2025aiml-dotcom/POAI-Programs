goal = "Pass Exam"

studied = False
assignment = False

while True:

    task = input("Enter completed task (study/assignment): ").strip().lower()

    if task == "study":
        studied = True
        print("Study completed.")

    elif task == "assignment":
        assignment = True
        print("Assignment completed.")

    else:
        print("Invalid Task")

    if studied and assignment:
        print("\n Goal Achieved:", goal)
        break
    else:
        print("Goal not achieved. Keep working!\n")