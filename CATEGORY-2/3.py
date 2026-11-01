import random

print("1. Static Environment")
print("2. Dynamic Environment")

choice = int(input("Enter your choice: "))

if choice == 1:

    number = 10

    if number > 5:
        print("Number is Greater than 5")

elif choice == 2:

    number = random.randint(1,10)

    print("Current Number:", number)

    if number > 5:
        print("Greater than 5")
    else:
        print("Less than or Equal to 5")

else:
    print("Invalid Choice")