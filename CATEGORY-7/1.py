colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

assignment = {}

def is_valid(node, color):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve():
    if len(assignment) == len(graph):
        return True

    node = next(n for n in graph if n not in assignment)

    for color in colors:
        if is_valid(node, color):
            assignment[node] = color

            if solve():
                return True

            del assignment[node]

    return False

if solve():
    print(assignment)
else:
    print("No solution")