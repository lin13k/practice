# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[start:' + str(self.start) + ' end:' + str(self.end) + ']'


class Solution(object):
    def insert(self, intervals, newInterval):
        left, right = [], []
        s, e = newInterval.start, newInterval.end
        for i in intervals:
            if i.end < s:
                left.append(i)
            elif i.start > e:
                right.append(i)
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right


def genNode(inputList):
    result = []
    for i in inputList:
        result.append(Interval(i[0], i[1]))
    return result


if __name__ == '__main__':
    print(Solution().insert(genNode([[1, 2], [3, 5], [
        6, 7], [8, 10], [12, 16]]), Interval(4, 9)))
