print("1. Discrete Environment")
print("2. Continuous Environment")

choice = int(input("Enter your choice: "))

if choice == 1:

    states = ["Red","Yellow","Green"]

    for state in states:
        print(state)

elif choice == 2:

    speed = 0

    while speed <= 100:
        print("Speed:", speed)
        speed += 20

else:
    print("Invalid Choice")