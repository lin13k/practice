# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        if k == 0:
            return head

        # count the list
        nodeCount = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            nodeCount += 1

        k = k % nodeCount
        if k == 0:
            return head

        newHead = head
        for i in range(nodeCount - k):
            if i == nodeCount - k - 1:
                node = newHead
                newHead = newHead.next
                node.next = None
            else:
                newHead = newHead.next
        tail.next = head
        return newHead
