# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        node = head

        while node.next is not None:
            tmpNode = node.next
            if tmpNode.val == node.val:
                node.next = tmpNode.next
            else:
                node = node.next

        return head
