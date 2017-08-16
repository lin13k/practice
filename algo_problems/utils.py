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