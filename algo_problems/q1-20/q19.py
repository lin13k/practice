# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def findEnd(head, nth):
            tmp = 0
            if head.next is not None:
                tmp = findEnd(head.next, nth)
                if tmp == nth:
                    head.next = head.next.next
            return tmp + 1

        tmp = findEnd(head, n)
        if tmp == n:
            return head.next
        return head
