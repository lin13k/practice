from heapq import heappush, heappushpop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        self.n = 0

    def addNum(self, num):
        if self.n % 2 == 0:
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        self.n += 1

    def findMedian(self):
        if self.n % 2 == 1:
            return self.large[0] + 0.0
        else:
            return (self.large[0] - self.small[0]) / 2.0


if __name__ == '__main__':
    testData = [4, 1, 2, 6, 7, 8, 3, 2, 1, 9]
    mf = MedianFinder()
    for i in range(len(testData)):
        print(sorted(testData[:i + 1]))
        mf.addNum(testData[i])
        print(mf.findMedian())
