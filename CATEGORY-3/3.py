import random
import math

random.seed(1)

values = [10, 25, 15, 40, 30, 80, 45, 20, 90, 35]

current = 0
best = current
temperature = 100

for i in range(10):

    if current == 0:
        next_position = 1
    elif current == len(values) - 1:
        next_position = current - 1
    else:
        next_position = random.choice([current - 1, current + 1])

    current_value = values[current]
    next_value = values[next_position]

    difference = next_value - current_value

    if difference > 0:
        current = next_position
        print("Better move:", values[current])

    else:
        probability = math.exp(difference / temperature)

        if random.random() < probability:
            current = next_position
            print("Worse move accepted:", values[current])
        else:
            print("Worse move rejected:", values[next_position])

    if values[current] > values[best]:
        best = current

    temperature = temperature * 0.9

print("\nBest value found:", values[best])
print("Global optimum:", max(values))