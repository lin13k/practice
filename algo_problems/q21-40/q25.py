# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        step = 0
        result = None
        groupHead = head
        preGroupHead = None
        while head:
            if step % k == 0:
                # setting up
                groupHead = head
            elif step % k == k - 1:
                # do reverse
                tmpNode = groupHead.next
                preNode = groupHead
                for i in range(k-1):
                    nextNode = tmpNode.next
                    tmpNode.next = preNode
                    preNode = tmpNode
                    tmpNode = nextNode
                groupHead.next = tmpNode
                head = groupHead
                if not result:
                    result = preNode
                else:
                    if preGroupHead: preGroupHead.next = preNode
                    preGroupHead = groupHead

            step += 1
            head = head.next
        return result



def genNodes(data):
    tmpNode = None
    preNode = None
    for i in range(len(data)-1, -1, -1):
        tmpNode = ListNode(data[i])
        tmpNode.next = preNode
        preNode = tmpNode
    return tmpNode


def convertNodesToList(dataNode):
    head = dataNode
    tmpLt = []
    while head is not None:
        tmpLt.append(head.val)
        head = head.next
    return tmpLt


if __name__ == '__main__':
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4]), 2)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4,5,6,7,8,9,10]), 2)))