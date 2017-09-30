# Definition for an interval.
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x.end)
        currentStart = intervals[-1].start
        currentEnd = intervals[-1].end
        i = len(intervals) - 2
        while i > -1:
            node = intervals[i]
            if currentStart <= node.end:
                intervals.pop(i + 1)
                currentStart = min(node.start, currentStart)
                node.end = currentEnd
                node.start = currentStart
            else:
                currentStart = node.start
                currentEnd = node.end
            i -= 1
        return intervals


def genNode(inputList):
    result = []
    for i in inputList:
        result.append(Interval(i[0], i[1]))
    return result


if __name__ == '__main__':
    print(len(Solution().merge(genNode([[1, 3], [2, 6], [8, 10], [15, 18]]))))
