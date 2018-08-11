class BST_Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

    def __repr__(self):
        return '[' + str(self.value) + ':' + str(self.count) + ']'


class BST:
    def __init__(self):
        self.root = BST_Node(None)

    def insert(self, value, node):
        if node.value is None:
            node.value = value
        elif node.value == value:
            node.count += 1
        elif node.value > value:
            if node.left is None:
                node.left = BST_Node(None)
            self.insert(value, node.left)
        elif node.value < value:
            if node.right is None:
                node.right = BST_Node(None)
            node.count += 1
            self.insert(value, node.right)

    def search(self, value, node):
        if node is None or node.value is None:
            return 0
        elif node.value == value:
            return node.count
        elif node.value > value:
            return node.count + self.search(value, node.left)
        elif node.value < value:
            return self.search(value, node.right)


class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bst = BST()
        result = 0
        for num in nums:
            tmp = bst.search(num * 2 + 1, bst.root)
            result += tmp
            bst.insert(num, bst.root)

        return result


if __name__ == '__main__':
    print(Solution().reversePairs([1, 3, 2, 3, 1]))
    # print(Solution().reversePairs([2, 4, 3, 5, 1]))
