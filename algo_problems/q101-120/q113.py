# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.recursive_find(root, sum, [], result)
        return result

    def recursive_find(self, node, sum, path, result):
        if node is None:
            return
        if node.val == sum and node.left is None and node.right is None:
            result.append(path + [node.val])
        self.recursive_find(node.left, sum - node.val, path + [node.val], result)
        self.recursive_find(node.right, sum - node.val, path + [node.val], result)
