# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        result = TreeNode(root.val)

        def helper(readNode, writeNode):
            if readNode.left is not None:
                writeNode.right = TreeNode(readNode.left.val)
                helper(readNode.left, writeNode.right)

            if readNode.right is not None:
                writeNode.left = TreeNode(readNode.right.val)
                helper(readNode.right, writeNode.left)

        helper(root, result)
        return result
