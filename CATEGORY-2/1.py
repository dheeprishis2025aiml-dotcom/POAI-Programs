rooms = {
    "A": "Clean",
    "B": "Dirty",
    "C": "Clean"
}

print("1. Fully Observable")
print("2. Partially Observable")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\nFully Observable Environment")

    for room, status in rooms.items():
        if status == "Dirty":
            print("Cleaning Room", room)
            rooms[room] = "Clean"

    print("Final State:", rooms)

elif choice == 2:
    print("\nPartially Observable Environment")

    room = "Dirty"

    if room == "Dirty":
        print("Cleaning current room...")
        room = "Clean"

    print("Current Room:", room)

else:
    print("Invalid Choice")