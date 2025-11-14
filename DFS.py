G = {
    'a': ['c'],
    'b': ['a', 'c', 'b'],
    'c': ['f', 'b'],
    'd': ['h', 'f'],
    'e': ['b', 'c', 'h'],
    'f': ['a', 'g'],
    'g': ['c'],
    'h': ['d'],
    'i': []
}

discovered = {}
finished = {}
time = 0

def dfs(node):
    global time
    if node not in discovered:
        # discovery time
        time += 1
        discovered[node] = time

        for neighbor in G[node]:
            if neighbor not in discovered:  # small optimization
                dfs(neighbor)

        # finish time
        time += 1
        finished[node] = time

# Run DFS from each node
for node in G:
    dfs(node)

print("Discovered times:", discovered)
print("Finished times:", finished)
