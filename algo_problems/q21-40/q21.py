# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        tmpLtA = l1 if l1.val < l2.val else l2
        tmpLtB = l1 if l1.val >= l2.val else l2
        root = None
        head = None
        while tmpLtB is not None and tmpLtA is not None:
            if tmpLtA.val > tmpLtB.val:
                tmpLtA, tmpLtB = tmpLtB, tmpLtA
            if head is not None:
                head.next = tmpLtA
            head = tmpLtA
            tmpLtA = tmpLtA.next
            if root is None:
                root = head
        if tmpLtB is not None:
            head.next = tmpLtB
        return root


def genNodes(data):
    tmpNode = None
    preNode = None
    for i in range(len(data)-1, -1, -1):
        tmpNode = ListNode(data[i])
        tmpNode.next = preNode
        preNode = tmpNode
    return tmpNode


def NodesToList(dataNode):
    head = dataNode
    tmpLt = []
    while head is not None:
        tmpLt.append(head.val)
        head = head.next
    return tmpLt


if __name__ == '__main__':
    l1data = [-10, -10, -9, -4, 1, 6, 6]
    l2data = [-7]

    print(NodesToList(Solution().mergeTwoLists(genNodes(l1data), genNodes(l2data))))
