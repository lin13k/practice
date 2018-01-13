# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        if root is None:
            return True
        node = root
        pre = None
        while node is not None or len(stack) != 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre is not None and node.val <= pre.val:
                return False
            pre = node
            node = node.right
        return True


if __name__ == '__main__':
