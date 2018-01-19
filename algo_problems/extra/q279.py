from collections import defaultdict


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        qTable = []
        while i <= n**0.5:
            i += 1
            qTable.append(i * i)
        # print(qTable)
        memo = defaultdict(lambda : n)
        memo[1] = 1
        memo[0] = 0
        for i in range(0, n + 1):
            for q in qTable:
                if q + i > n:
                    break
                memo[i + q] = min(memo[i + q], memo[i] + 1)
        # print(memo)
        return memo[n]

if __name__ == '__main__':
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))
    print(Solution().numSquares(16))
    print(Solution().numSquares(6166))
    print(Solution().numSquares(60166))
    
