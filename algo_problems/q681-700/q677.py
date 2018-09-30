from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.num = 0
        self.sum = 0
        self.children = defaultdict(lambda: TrieNode())

    def addChild(self, key, value):
        # self.num += value
        # if len(key) <= 1:
        #     self.children[key[0:1]].num += value
        # else:
        #     self.children[key[0:1]].addChild(key[1:], value)

        change = 0
        if len(key) <= 0:
            change = value - self.num
            self.num = value
        else:
            change = self.children[key[0:1]].addChild(key[1:], value)
        self.sum += change
        return change

    def getChild(self, key):
        if len(key) <= 0:
            return self.sum
        return self.children[key[0:1]].getChild(key[1:])


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.root.addChild(key, val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.root.getChild(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
if __name__ == '__main__':
    obj = MapSum()
    obj.insert('apple', 2)
    obj.insert('ap', 3)
    obj.insert('ap', 4)
    print(obj.sum('ap'))
    print(obj.sum('a'))
    print(obj.sum('c'))
