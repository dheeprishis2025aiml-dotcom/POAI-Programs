roomA = "Dirty"
roomB = "Dirty"

while True:

    room = input("\nEnter Room (A/B): ").upper()

    if room == "A":

        if roomA == "Dirty":
            print("Cleaning Room A")
            roomA = "Clean"

        else:
            print("Room A is already Clean")

    elif room == "B":

        if roomB == "Dirty":
            print("Cleaning Room B")
            roomB = "Clean"

        else:
            print("Room B is already Clean")

    else:
        print("Invalid Room")

    print("\nCurrent Room Status")
    print("Room A:", roomA)
    print("Room B:", roomB)

    choice = input("\nContinue? (yes/no): ").lower()

    if choice == "no":
        break