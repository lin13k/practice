class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(self.catalanNumber(n - 1))

    def catalanNumber(self, n):
        if n == 0:
            return 1
        return self.catalanNumber(n - 1) * (2 * ((2 * n) + 1) / (n + 2.0))


if __name__ == '__main__':
    print(Solution().numTrees(2))
    print(Solution().numTrees(3))
    print(Solution().numTrees(4))
