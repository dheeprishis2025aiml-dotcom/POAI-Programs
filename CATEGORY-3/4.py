values = [10, 25, 15, 40, 30, 80, 45, 20, 90, 35]

beam = [0, 3, 6]
k = 3

for i in range(5):

    candidates = []

    for current in beam:

        if current > 0:
            candidates.append(current - 1)

        if current < len(values) - 1:
            candidates.append(current + 1)

    candidates.sort(key=lambda x: values[x], reverse=True)

    beam = candidates[:k]

    print("Beam:", [values[x] for x in beam])

print("Best value:", max(values[x] for x in beam))