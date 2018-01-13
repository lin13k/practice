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
        tmpList = []
        self.dfsPop(root, tmpList)
        for i in range(len(tmpList) - 1):
            if tmpList[i] >= tmpList[i + 1]:
                return False
        return True

    def dfsPop(self, root, result):
        if root is None:
            return
        if root.left is not None:
            self.dfsPop(root.left, result)

        result.append(root.val)

        if root.right is not None:
            self.dfsPop(root.right, result)


if __name__ == '__main__':
