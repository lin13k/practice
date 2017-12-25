class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0

        dpTable = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dpTable[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dpTable[i][j] = 1
                    elif i == 0:
                        dpTable[i][j] = dpTable[i][j - 1]
                    elif j == 0:
                        dpTable[i][j] = dpTable[i - 1][j]
                    else:
                        dpTable[i][j] = dpTable[i][j - 1] + dpTable[i - 1][j]
        
        # print(dpTable)
        return dpTable[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0, 0]]))
    print(Solution().uniquePathsWithObstacles(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]))
