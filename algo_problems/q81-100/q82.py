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
        if head is None or head.next is None:
            return head

        root = None
        pn = None
        node = head
        deleteFlag = False
        while node.next is not None:
            tmpNode = node.next
            if node.val == tmpNode.val:
                deleteFlag = True
            else:
                if deleteFlag:
                    deleteFlag = False
                    if pn is not None:
                        pn.next = tmpNode
                else:
                    pn = node
                    if root is None:
                        root = pn
            node = node.next
        if deleteFlag:
            if pn is not None:
                pn.next = None
            return root
        else:
            if root is None:
                return node
            else:
                return root


if __name__ == '__main__':
    Solution().deleteDuplicates()

    # 112
    # 123
    # 122
