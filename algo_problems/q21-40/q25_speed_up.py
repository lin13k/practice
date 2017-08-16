# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        step = 0
        result = head
        groupHead = head
        preGroupHead = None
        firstFlag = True
        while head:
            if step % k == 0:
                groupHead = head
            elif step % k == k - 1:
                tmpNode = groupHead.next
                preNode = groupHead
                nextNode = None
                for i in range(k-1):
                    nextNode = tmpNode.next
                    tmpNode.next = preNode
                    preNode = tmpNode
                    tmpNode = nextNode
                groupHead.next = tmpNode
                if preGroupHead:
                    preGroupHead.next = preNode
                if firstFlag:
                    result = preNode
                    firstFlag = False
                preGroupHead = groupHead
                head = groupHead

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
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1]), 1)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4]), 2)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4,5,6,7,8,9,10]), 2)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4]), 3)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4,5,6,7,8,9,10]), 3)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4,5,6,7,8,9,10]), 4)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([1,2,3,4,5]), 3)))