
def zip_longest(*args):
    maxLength = 0
    result = []
    for i in range(len(args)):
        maxLength = max(maxLength, len(args[i]))
    for j in range(maxLength):
        tmp = []
        for i in range(len(args)):
            if j < len(args[i]):
                tmp.append(args[i][j])
            else:
                tmp.append(None)
        result.append(tmp)
    return result


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        mergedData = []
        list(map(mergedData.extend, list(zip_longest(v1, v2))))
        self.data = list(filter(lambda x: x is not None, mergedData))
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            raise Exception('no next')
        self.index += 1
        return self.data[self.index - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index in range(len(self.data))



# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    
    z = ZigzagIterator([1, 2], [3, 4, 5, 6])
    print(z.hasNext())
    while z.hasNext():
        print(z.next())
    