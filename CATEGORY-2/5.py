import random

print("1. Deterministic Environment")
print("2. Stochastic Environment")

choice = int(input("Enter your choice: "))

if choice == 1:

    number = 5
    result = number * 2

    print("Result:", result)

elif choice == 2:

    result = random.randint(1,10)

    print("Random Number:", result)

else:
    print("Invalid Choice")