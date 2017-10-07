class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num):
        left = 0
        right = len(self.data) - 1

        found = False
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            item = self.data[mid]
            if item > num:
                right -= 1
            elif item < num:
                left += 1
            else:
                found = True
                break

        if found:
            self.data.insert(mid, num)
        else:
            self.data.insert(left, num)

    def findMedian(self):
        if len(self.data) % 2 == 1:
            return self.data[len(self.data) // 2]
        else:
            return (self.data[len(self.data) // 2 - 1] + self.data[len(self.data) // 2]) / 2.0


if __name__ == '__main__':
    testData = [4, 1, 2, 6, 7, 8, 3, 2, 1, 9]
    mf = MedianFinder()
    for i in testData:
        mf.addNum(i)
    print(mf.data)
    print(mf.findMedian())
