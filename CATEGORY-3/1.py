import random

values = [10, 25, 15, 40, 30, 80, 45, 20, 90, 35]

current = random.randint(0, len(values) - 1)

for i in range(10):

    start = max(0, current - 2)
    end = min(len(values), current + 3)

    nearby = values[start:end]

    best = max(nearby)
    best_position = start + nearby.index(best)

    print("Current:", values[current])
    print("Nearby:", nearby)

    if values[best_position] > values[current]:
        current = best_position
        print("Move to:", values[current])
    else:
        print("Local optimum reached")
        break

print("\nFinal value:", values[current])