graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'

front = {start}
back = {goal}

while front and back:

    next_front = set()

    for node in front:
        for neighbor in graph[node]:
            if neighbor in back:
                print("Found")
                exit()
            next_front.add(neighbor)

    front = next_front

    for node in back:
        for parent in graph:
            if node in graph[parent]:
                if parent in front:
                    print("Found")
                    exit()
                next_front.add(parent)

    back = next_front