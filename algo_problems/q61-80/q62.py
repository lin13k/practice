class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dpTable = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            dpTable[i][0] = 1

        for i in range(n):
            dpTable[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dpTable[i][j] = dpTable[i - 1][j] + dpTable[i][j - 1]

        return dpTable[-1][-1]
