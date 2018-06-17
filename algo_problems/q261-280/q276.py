class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n <= 0 or k <= 0:
            return 0
        if n == 1:
            return k
        diffN = k * (k - 1)
        sameN = k
        for i in range(2, n):
            tmp = diffN
            diffN = (diffN + sameN) * (k - 1)
            sameN = tmp
        return diffN + sameN


if __name__ == '__main__':
    print(Solution().numWays(2, 2))
    print(Solution().numWays(3, 2))
    print(Solution().numWays(4, 2))
