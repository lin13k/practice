# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[start:' + str(self.start) + ' end:' + str(self.end) + ']'


class Solution(object):
    def insert(self, intervals, newInterval):

        if len(intervals) == 0:
            return [newInterval]

        pNode = newInterval

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        startIndex = intervals.index(pNode)
        if startIndex > 0 and intervals[startIndex - 1].end >= pNode.start:
            pNode.start = intervals[startIndex - 1].start
            pNode.end = max(intervals[startIndex - 1].end, pNode.end)
            intervals.pop(startIndex - 1)
            startIndex -= 1

        # print(intervals)
        intervals = [intervals.pop(startIndex)] + intervals
        intervals.sort(key=lambda x: x.end)
        endIndex = intervals.index(pNode)
        if endIndex < len(intervals)-1 and intervals[endIndex + 1].start <= pNode.end:
            pNode.end = intervals[endIndex + 1].end
            intervals.pop(endIndex + 1)
        # print(intervals)

        # print(startIndex, endIndex)
        return intervals[:startIndex] + [pNode] + intervals[endIndex + 1:]


def genNode(inputList):
    result = []
    for i in inputList:
        result.append(Interval(i[0], i[1]))
    return result


if __name__ == '__main__':
    print(Solution().insert(genNode([[1, 2], [3, 5], [
        6, 7], [8, 10], [12, 16]]), Interval(4, 9)))
