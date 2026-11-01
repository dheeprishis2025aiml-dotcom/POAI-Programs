print("Study Methods")
print("1. Self Study - Utility 60")
print("2. YouTube - Utility 80")
print("3. Coaching - Utility 95")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    utility = 60
    method = "Self Study"

elif choice == 2:
    utility = 80
    method = "YouTube"

elif choice == 3:
    utility = 95
    method = "Coaching"

else:
    print("Invalid Choice")
    exit()

print("\nSelected Method:", method)
print("Utility:", utility)

if utility >= 90:
    print("Best Choice!")

elif utility >= 70:
    print("Good Choice!")

else:
    print("Average Choice.")