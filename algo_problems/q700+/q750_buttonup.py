class Solution(object):
    # sx, sy        ex, sy
    # sx, ey        ex, ey
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        if len(grid) <= 1 or len(grid[0]) <= 1:
            return 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(i + 1, n):
                pair = 0
                for k in range(m):
                    if grid[i][k] == 1 and grid[j][k]:
                        pair += 1
                cnt += (pair * (pair - 1)) // 2
        return cnt


if __name__ == '__main__':
    print(Solution().countCornerRectangles(
        [[0, 1, 0],
         [1, 0, 1],
         [1, 0, 1],
         [0, 1, 0]]))
    print(Solution().countCornerRectangles(
        [[1, 1, 0],
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 0]]))
    print(Solution().countCornerRectangles(
        [[1, 1, 1],
         [1, 1, 1]]))
