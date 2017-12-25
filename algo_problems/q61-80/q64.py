class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        dpTable = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dpTable[i][j] = grid[i][j]
                elif i == 0:
                    dpTable[i][j] = dpTable[i][j - 1] + grid[i][j]
                elif j == 0:
                    dpTable[i][j] = dpTable[i - 1][j] + grid[i][j]
                else:
                    dpTable[i][j] = min(
                        dpTable[i][j - 1] + grid[i][j],
                        dpTable[i - 1][j] + grid[i][j],
                    )
        print(dpTable)
        return dpTable[-1][-1]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, 1, 1],
        [2, 2, 1]
    ]))
