# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        def swapFunc(nodeHead, preNode, headFlag):
            if nodeHead is not None:
                if nodeHead.next is not None:
                    nodeB = nodeHead.next
                    nodeHead.next = nodeB.next
                    nodeB.next = nodeHead
                    if preNode:
                        preNode.next = nodeB
                    swapFunc(nodeHead.next, nodeHead, False)
                    if headFlag:
                        return nodeB
                else:
                    if headFlag:
                        return nodeHead
        head = swapFunc(head, None, True)
        return head


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

    print(NodesToList(Solution().swapPairs(genNodes([1,2,3,4]))))
    print(NodesToList(Solution().swapPairs(genNodes([1,2,3,4,5]))))
    print(NodesToList(Solution().swapPairs(genNodes([1,2,3,4,5,6]))))