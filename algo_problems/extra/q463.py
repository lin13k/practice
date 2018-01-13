class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        m = len(grid)
        for i in range(len(grid)):
            n = len(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # check up
                    if i == 0 or grid[i - 1][j] != 1:
                        result += 1
                    # check down
                    if i == m - 1 or grid[i + 1][j] != 1:
                        result += 1
                    # check left
                    if j == 0 or grid[i][j - 1] != 1:
                        result += 1
                    # check right
                    if j == n - 1 or grid[i][j + 1] != 1:
                        result += 1
        return result

if __name__ == '__main__':
    print(Solution().islandPerimeter([
        [0,0,0,0],
        [0,1,1,1],
        [0,0,1,0],
        [0,0,0,0]
        ]))