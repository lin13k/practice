# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.recursiveGenTrees(1, n)

    def recursiveGenTrees(self, startIndex, endIndex):
        if startIndex > endIndex:
            return []
        if startIndex == endIndex:
            return [TreeNode(startIndex)]

        result = []
        for i in range(startIndex, endIndex + 1):
            leftSubTrees = self.recursiveGenTrees(startIndex, i - 1)
            rightSubTrees = self.recursiveGenTrees(i + 1, endIndex)

            if len(leftSubTrees) != 0 and len(rightSubTrees) != 0:
                for leftRootNode in leftSubTrees:
                    for rightRootNode in rightSubTrees:
                        rootNode = TreeNode(i)
                        rootNode.left = leftRootNode
                        rootNode.right = rightRootNode
                        result.append(rootNode)
            else:
                for leftRootNode in leftSubTrees:
                    rootNode = TreeNode(i)
                    rootNode.left = leftRootNode
                    result.append(rootNode)
                for rightRootNode in rightSubTrees:
                    rootNode = TreeNode(i)
                    rootNode.right = rightRootNode
                    result.append(rootNode)
        return result


if __name__ == '__main__':
    print(len(Solution().generateTrees(1)))
    print(len(Solution().generateTrees(2)))
    print(len(Solution().generateTrees(3)))
    print(len(Solution().generateTrees(4)))
