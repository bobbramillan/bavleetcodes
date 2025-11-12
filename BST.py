"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""
#typically i would use the above esp in C but for illustration purposes im doing the below

BST_index = {}
BST_parent = {}
BST_left = {}
BST_right = {}

#for the multiple peaks question use a max heap

nodes_in_level = {}

def insert(val, root, level):

    if val <= root: 
        if BST_left[root] is None:
            BST_left[root] = val
            BST_parent[val] = root

            BST_left[val] = None
            BST_right[val] = None
            if level not in nodes_in_level:
                nodes_in_level[level] = []
            nodes_in_level[level].append(val)
        else:
            level += 1
            insert(val, BST_left[root], level)
    elif val > root:
        if BST_right[root] is None:
            BST_right[root] = val
            BST_parent[val] = root

            BST_left[val] = None
            BST_right[val] = None
            if level not in nodes_in_level:
                nodes_in_level[level] = []
            nodes_in_level[level].append(val)
        else:
            level += 1
            insert(val, BST_right[root], level)
    else:
        return


def build_bst_from_array(queue):
    root = queue[0]  
    BST_parent[root] = None
    BST_left[root] = None
    BST_right[root] = None
    BST_index[root] = 0
    level = 0
    nodes_in_level[level] = [root]
    level += 1

    for i in range(1, len(queue)):
        val = queue[i]
        BST_index[val] = i
        insert(val, root, level)

    print("\nBST Parent:", BST_parent)
    print("\nNodes in Level", nodes_in_level)


# Example usage aka my input array
queue = [1, 3, 2, 5, 4, 7, 6]
build_bst_from_array(queue)





