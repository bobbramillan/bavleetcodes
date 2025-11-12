# Directed Graph, outgoing arrows (neighbor nodes) are values of key(aka node)
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
dtime = 0
ftime = 0

def dfs(node):
    global dtime, ftime #cuz Python for some reason treats variables in a function as local
    if node not in discovered:
        # record discovery time
        dtime += 1
        discovered[node] = dtime
        for value in G[node]:
            dfs(value)
        # record finish time
        ftime += 1
        finished[node] = ftime

# Run DFS from each node (handles disconnected graph)
for node in G:
    dfs(node)

print("\nDiscovered times:", discovered)
print("\nFinished times:", finished)
print("\n")
