print("1. Episodic Environment")
print("2. Sequential Environment")

choice = int(input("Enter your choice: "))

if choice == 1:

    images = ["Cat","Dog","Bird"]

    for image in images:
        if image == "Cat":
            print("Cat Found")
        else:
            print("Not a Cat")

elif choice == 2:

    position = 0
    commands = ["Right","Right","Left","Right"]

    for move in commands:
        if move == "Right":
            position += 1
        else:
            position -= 1

    print("Final Position:", position)

else:
    print("Invalid Choice")