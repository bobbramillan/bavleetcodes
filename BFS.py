# --- Directed Graph ---
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
start = 'h'

# the print \n is only for aesthetics

def bfs(G, start):
    # Initialize data structures
    queue = []          
    dist = {}           
    pred = {}
    print("\n")           

    # Step 1: setup start node
    dist[start] = 0
    pred[start] = None
    queue.append(start)

    # Step 2: start traversal while queue is not empty
    while queue:
        print("Queue:", queue)
        x = queue.pop(0)           # the # values in here depend on the key and if they havent been seen yet
        y = dist[x] + 1            # set counter as a 1 increment of distance

        # Step 3: explore neighbors, (for each z in ..) is one way to think abt it
        for z in G[x]:
            # if we haven't already seen z, u could also do (if z not in pred)
            if z not in dist:
                dist[z] = y        # assign distance
                pred[z] = x        # assign predecessor
                queue.append(z)    # add z to queue

    # Step 4: when done, print both or change to return
    print("\nDistance:", dist)
    print("\nPredecessor:", pred)

bfs(G, start)
print("\n")
