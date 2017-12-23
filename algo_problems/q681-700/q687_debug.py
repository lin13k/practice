# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            root = stringToTreeNode(line)

            ret = Solution().longestUnivaluePath(root)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    root = stringToTreeNode('[1,4,5,4,4,5]')
    ret = Solution().longestUnivaluePath(root)
    out = str(ret)
    print(out)

    # root = stringToTreeNode('[1,1,1,1,4,5]')
    # ret = Solution().longestUnivaluePath(root)
    # out = str(ret)
    # print(out)
