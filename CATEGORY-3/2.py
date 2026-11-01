import random

values = [10, 25, 15, 40, 30, 80, 45, 20, 90, 35]

current = random.randint(0, len(values) - 1)

for i in range(5):

    print("\nCurrent position:", current)
    print("Current value:", values[current])

    if random.choice([True, False]):
        print("Exploration")

        best = max(values)
        current = values.index(best)

        print("Best value in entire search space:", best)

    else:
        print("Exploitation")

        start = max(0, current - 2)
        end = min(len(values), current + 3)

        nearby = values[start:end]

        best = max(nearby)
        current = start + nearby.index(best)

        print("Nearby values:", nearby)
        print("Best nearby value:", best)

print("\nFinal position:", current)
print("Final value:", values[current])