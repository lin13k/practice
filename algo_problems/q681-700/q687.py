# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]

        def innerFunction(root):
            int_sum = 0
            left = 0
            right = 0
            if root is None:
                return 0

            if root.left:
                left_sum = innerFunction(root.left)
                if root.left.val == root.val:
                    int_sum += left_sum + 1
                    left = left_sum + 1
            if root.right:
                right_sum = innerFunction(root.right)
                if root.right.val == root.val:
                    int_sum += right_sum + 1
                    right = right_sum + 1
            result[0] = max(result[0], int_sum)
            return max(left, right)
        innerFunction(root)
        return result[0]
