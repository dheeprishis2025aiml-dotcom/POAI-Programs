import random

print("1. Known Environment")
print("2. Unknown Environment")

choice = int(input("Enter your choice: "))

if choice == 1:

    destination = 10
    position = 0

    while position < destination:
        position += 1
        print("Moving to", position)

    print("Destination Reached")

elif choice == 2:

    position = 0

    while True:
        step = random.randint(1,3)
        position += step

        print("Moved to", position)

        if position >= 10:
            print("Destination Found")
            break

else:
    print("Invalid Choice")