class Solution(object):
    class Node:
        def __init__(self, val='', parent=None):
            self.val = val
            self.children = {}
            if parent:
                tmp = parent.children.get(self.val, self)
                self.__dict__ = tmp.__dict__
                parent.children[self.val] = self

        def __str__(self):
            return '{val: %s, children: %s}' % (self.val, self.children)

        def __repr__(self):
            return self.__str__()

    def longestCommonPrefix(self, strs):
        rootNode = Solution.Node(val='root')
        endFlag = "#"
        for s in strs:
            self.buildTree(s + endFlag, rootNode)

        print(rootNode)
        tmpNode = rootNode
        result = []
        while tmpNode:
            result.append(tmpNode.val)
            if len(tmpNode.children) != 1:
                break
            tmpNode = list(tmpNode.children.values())[0]

        return ''.join(result[1:]).replace(endFlag, "")

    def buildTree(self, str, rootNode):
        tmpNode = rootNode
        for i in range(len(str)):
            tmpNode = Solution.Node(val=str[i], parent=tmpNode)
        return rootNode

if __name__ == '__main__':
    a = Solution.Node(val='a')
    b = Solution.Node(val='b', parent=a)
    c = Solution.Node(val='c', parent=b)
    b2 = Solution.Node(val='b', parent=a)
    print(a)
    # assert(str(a) ==
    #        "{val: a, children: " +
    #        "{'b': {val: b, children: {'c': {val: c, children: {}}}}}}")

    # r = Solution.Node(val='root')
    # Solution().buildTree('abcdefg', r)
    # print(r)

    print(Solution().longestCommonPrefix([
        'abc',
        'abcd',
        'abcde'
    ]))

    print(Solution().longestCommonPrefix([
        ""
    ]))
