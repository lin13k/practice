class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        n = len(grid)
        if n == 0:
            return result
        m = len(grid[0])
        q = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(m):
                tmp = 0
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
                while len(q) != 0:
                    x, y = q.pop(0)
                    tmp += 1
                    for direct in directions:
                        tmpx = x + direct[0]
                        tmpy = y + direct[1]
                        if (tmpx >= 0 and tmpx <= n - 1 and
                            tmpy >= 0 and tmpy <= m - 1 and
                                grid[tmpx][tmpy] == 1):
                            q.append((tmpx, tmpy))
                            grid[tmpx][tmpy] = 0
                result = max(result, tmp)
        return result
