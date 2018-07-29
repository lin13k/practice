from collections import Counter


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[0] != 0:
            return False
        table = {stones[i]: [] for i in range(len(stones))}
        table[0].append(0)
        for i in range(len(stones)):
            cur = table[stones[i]]
            for j in cur:
                if (j - 1 > 0 and
                        stones[i] + j - 1 in table):
                    table[stones[i] + j - 1].append(j - 1)
                if j > 0 and stones[i] + j in table:
                    table[stones[i] + j].append(j)
                if j + 1 > 0 and stones[i] + j + 1 in table:
                    table[stones[i] + j + 1].append(j + 1)
        return len(table[stones[-1]]) > 0


if __name__ == '__main__':
    print(Solution().canCross(
        [0, 1, 3, 5]))
    print(Solution().canCross(
        [0, 1, 3, 5, 6, 8, 12, 17]))
    print(Solution().canCross(
        [0, 1, 2, 3, 4, 8, 9, 11]))
    print(Solution().canCross(
        [0, 1, 3, 4, 5, 7, 9, 10, 12]))
