from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        cntDict = OrderedCounter(T)
        result = []
        for c in S:
            if c in cntDict:
                result.append(c * cntDict[c])
                cntDict.pop(c)
        for key, value in cntDict.items():
            result.append(key * value)

        return ''.join(result)


if __name__ == '__main__':
    print(Solution().customSortString('acb', 'abcd'))
    print(Solution().customSortString('ad', 'abcd'))
    print(Solution().customSortString('', 'abcd'))
