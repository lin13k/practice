# https://leetcode.com/problems/add-two-numbers/#/description
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        rootNode = None
        preNode = None
        while True:
            preNode = l1
            if rootNode is None:
                rootNode = l1
            self.addNumberToNode(l1, l2.val)
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l2 is None:
                return rootNode
            elif l2 is None:
                return rootNode
            elif l1 is None:
                preNode.next = l2
                return rootNode
            

    def addNumberToNode(self, node, num):
        tmpN = node.val + num
        node.val = tmpN % 10
        if tmpN > 9:
            node.next = ListNode(0) if node.next is None else node.next
            self.addNumberToNode(node.next, 1)


if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    r = Solution().addTwoNumbers(a, b)
    print(r)

    a = ListNode(0)
    b = ListNode(7)
    b.next = ListNode(3)
    r = Solution().addTwoNumbers(a, b)
    print(r)
