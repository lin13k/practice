class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


def findLastNNode(rootNode, n):
    result = []

    def helpFunction(rootNode, n):
        if rootNode.next is None:
            return 1
        tmp = helpFunction(rootNode.next, n) + 1
        if tmp == n:
            result.append(rootNode.value)
        return tmp
    helpFunction(rootNode, n)
    return result[0]


def listToLinkedNodes(lst):
    head = None
    lastNode = None
    for i in lst:
        node = Node(i)
        if head is None:
            head = node
        else:
            lastNode.next = node
        lastNode = node
    return head


def printLinkedNodes(rootNode):
    while rootNode is not None:
        print(rootNode.value)
        rootNode = rootNode.next


if __name__ == '__main__':
    a = listToLinkedNodes([1, 2, 3, 4, 5])
    printLinkedNodes(a)

    print(findLastNNode(a, 3))
