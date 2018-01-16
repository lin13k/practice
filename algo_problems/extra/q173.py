# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._stack = []
        self.pushNodes(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self._stack) != 0

    def next(self):
        """
        :rtype: int
        """
        tmpNode = self._stack.pop()
        self.pushNodes(tmpNode.right)
        return tmpNode.val

    def pushNodes(self, node):
        while node is not None:
            self._stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
