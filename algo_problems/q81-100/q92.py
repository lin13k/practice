# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        node = head
        if node is None:
            return head

        reverseFlag = False
        rTail = None
        rHead = None
        pre = None
        while node is not None:
            nextNode = node.next
            m -= 1
            n -= 1
            if m == 1:
                pre = node
            if m == 0:
                # start reverse
                reverseFlag = True

            if reverseFlag:
                if rTail is None:
                    rTail = node
                    rHead = node
                else:
                    node.next = rHead
                    rHead = node

            node = nextNode
            if n == 0:
                # end reverse
                reverseFlag = False
                break
        if pre is not None:
            pre.next = rHead
        rTail.next = node
        if pre is None:
            return rHead
        else:
            return head
