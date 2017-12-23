class ValueNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class ContactBook:
    rootNode = ValueNode()

    def add(self, contact):
        cNode = self.rootNode
        cNode.count += 1
        for i in range(len(contact)):
            if contact[i] in cNode.children:
                cNode = cNode.children[contact[i]]
            else:
                tmp = ValueNode()
                cNode.children[contact[i]] = tmp
                cNode = tmp
            cNode.count += 1

    def count(self, keyword):
        cNode = self.rootNode
        for i in range(len(keyword)):
            if keyword[i] not in cNode.children:
                return 0
            cNode = cNode.children[keyword[i]]
        return cNode.count


n = int(input().strip())
cbook = ContactBook()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        cbook.add(contact)
    elif op == 'find':
        print(cbook.count(contact))
    else:
        raise Exception('unknown operation')

# if __name__ == '__main__':
#     cbook = ContactBook()
#     cbook.add('hack')
#     cbook.add('hackerrank')
#     print(cbook.count('hac'))
#     print(cbook.count('hak'))
