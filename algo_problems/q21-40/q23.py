# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


from heapq import heappop, heappush


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heapLt = []
        valueLt = []
        for node in lists:
            if node:
                heappush(heapLt, (node.val, node.next))

        while len(heapLt) != 0:
            tmp = heappop(heapLt)
            valueLt = [tmp[0]] + valueLt
            if tmp[1]:
                heappush(heapLt, (tmp[1].val, tmp[1].next))
        return self.listToNodeList(valueLt)

    def listToNodeList(self, lt):
        # lt.reverse()
        head = None
        for i in lt:
            tmpNode = ListNode(i)
            tmpNode.next = head
            head = tmpNode
        return head
