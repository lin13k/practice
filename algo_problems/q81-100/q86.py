# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        leftRoot = None
        rightRoot = None
        leftNode = None
        rightNode = None
        node = head
        while node is not None:
            print(node.val)
            if node.val < x:
                if leftRoot is None:
                    leftRoot = node
                if leftNode is not None:
                    leftNode.next = node
                leftNode = node
            else:
                if rightRoot is None:
                    rightRoot = node
                if rightNode is not None:
                    rightNode.next = node
                rightNode = node
            node = node.next

        if leftNode is not None:
            leftNode.next = rightRoot
            if rightNode is not None:
                rightNode.next = None
            return leftRoot
        else:
            if rightNode is not None:
                rightNode.next = None
            return rightRoot

if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(1)
    a.next = b

    Solution().partition(a, 2)
