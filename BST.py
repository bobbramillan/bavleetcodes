"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""
#typically i would use the above struct esp in C but for illustration purposes im doing the below


BST = {}
BST_index = {}

def insert(val, root):
    curr = root

    while True:
        left, right = BST[curr]  # always 2 elements

        # go left
        if val <= curr:
            if left is None:
                # insert here
                BST[curr][0] = val
                BST[val] = [None, None]
                return
            curr = left

        # go right
        else:
            if right is None:
                # insert here
                BST[curr][1] = val
                BST[val] = [None, None]
                return
            curr = right


def build_bst_from_array(arr):
    root = arr[0]

    BST[root] = [None, None]
    BST_index[root] = 0

    for i in range(1, len(arr)):
        val = arr[i]
        BST_index[val] = i
        insert(val, root)

    return BST, BST_index


# Example usage
queue = [1, 3, 2, 5, 4, 7, 6]
BST, BST_index = build_bst_from_array(queue)

print("\nBST =", BST)
print("\nBST_index =", BST_index)
print("\n")