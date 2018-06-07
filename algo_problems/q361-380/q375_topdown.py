
# 1 - > 0
# 2 - > 1
# 3 - > 2
# 4 - > 2 + 3  - > 1 + 3
# 5 - > 3 + 4
# 6 - > 3 + 5
# 7 - > 4 + 6
# 8 - > 4 + 6 + 7 - > 4 + 5 + 7
# 9 - > 5 + 7 + 8 - > 5 + 6 + 8

import sys


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [[0 for i in range(n + 1)] for j in range(n + 1)]
        return self.dp(table, 1, n)

    def dp(self, table, s, e):
        if s >= e:
            return 0
        if table[s][e] != 0:
            return table[s][e]
        result = sys.maxsize
        for i in range(s, e + 1):
            tmp = i + max(self.dp(table, s, i - 1), self.dp(table, i + 1, e))
            result = min(result, tmp)
        table[s][e] = result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.getMoneyAmount(1))
    print(s.getMoneyAmount(2))
    print(s.getMoneyAmount(3))
    print(s.getMoneyAmount(4))
    print(s.getMoneyAmount(5))
    print(s.getMoneyAmount(6))
    print(s.getMoneyAmount(7))
    print(s.getMoneyAmount(8))
    print(s.getMoneyAmount(9))
