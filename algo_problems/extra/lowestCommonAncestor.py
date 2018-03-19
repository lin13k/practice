# Python program to find LCA of n1 and n2 using one
# traversal of Binary tree

# A binary tree node


class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree


def findLCA(root, n1, n2):

    def helper(node, n1, n2):
        if node.key == n1 or node.key == n2:
            return node
        leftLCA = helper(node.left, n1, n2) if node.left is not None else None
        rightLCA = helper(node.right, n1, n2) if node.right is not None else None
        if leftLCA and rightLCA:
            return node
        if leftLCA:
            return leftLCA
        if rightLCA:
            return rightLCA
        return None
    return helper(root, n1, n2)

# Driver program to test above function


# Let us create a binary tree given in the above example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ", findLCA(root, 4, 5).key)
print("LCA(4,6) = ", findLCA(root, 4, 6).key)
print("LCA(3,4) = ", findLCA(root, 3, 4).key)
print("LCA(2,4) = ", findLCA(root, 2, 4).key)
