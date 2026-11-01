import random

variables = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']

constraints = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D')
]

assignment = {
    var: random.choice(colors) for var in variables
}

def conflicts():
    return sum(
        assignment[a] == assignment[b]
        for a, b in constraints
    )

def solve():
    for _ in range(1000):
        if conflicts() == 0:
            return True

        a, b = random.choice(constraints)
        variable = random.choice([a, b])

        old_color = assignment[variable]
        best_color = old_color
        best_score = conflicts()

        for color in colors:
            assignment[variable] = color
            score = conflicts()

            if score < best_score:
                best_score = score
                best_color = color

        assignment[variable] = best_color

    return conflicts() == 0

if solve():
    print("Solution:", assignment)
else:
    print("No solution found")