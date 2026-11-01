light_condition = input("Enter room condition (Dark/Bright): ").strip().lower()

if light_condition == "dark":
    print("Turning ON the Light")

elif light_condition == "bright":
    print("Turning OFF the Light")

else:
    print("Invalid Input")