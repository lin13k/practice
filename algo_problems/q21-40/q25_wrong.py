# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):

        def count(head):
            if not head.next:
                return 1
            else:
                return count(head.next) + 1


        def revFunc(head, preNode, k, root):
            if k > 0 and head:
                nextNode = head.next
                if preNode:
                    head.next = preNode
                return revFunc(nextNode, head, k-1, root)
            else:
                root.next = head
                if not head: return preNode
                return preNode

        if head:
            nodesN = count(head)
            if nodesN < k:
                return head

            return revFunc(head, None, k, head)
        else:
            return None

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
    # print(convertNodesToList(Solution().reverseKGroup(genNodes([1]), 2)))
    # print(convertNodesToList(Solution().reverseKGroup(genNodes([1, 2]), 2)))
    # print(convertNodesToList(Solution().reverseKGroup(genNodes([1]), 1)))
    print(convertNodesToList(Solution().reverseKGroup(genNodes([]), 1)))