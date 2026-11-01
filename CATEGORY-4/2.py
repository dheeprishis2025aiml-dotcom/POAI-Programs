graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

stack = ['A']
visited = []

while stack:
    node = stack.pop()

    if node not in visited:
        visited.append(node)
        stack.extend(reversed(graph[node]))

print(visited)