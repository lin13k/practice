class Solution(object):
    # sx, sy        ex, sy
    # sx, ey        ex, ey
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        if len(grid) <= 1 or len(grid[0]) <= 1:
            return 0
        self.table = {}
        r = self.helper(0, 0, len(grid) - 1, len(grid[0]) - 1)
        return r

    def helper(self, sx, sy, ex, ey):
        n = 0
        if sx >= ex or sy >= ey:
            return 0
        if (sx, sy, ex, ey) in self.table:
            return 0
        if (self.grid[sx][sy] and self.grid[ex][sy] and
                self.grid[sx][ey] and self.grid[ex][ey]):
            n += 1
        n += self.helper(sx, sy, ex, ey - 1)
        n += self.helper(sx, sy, ex - 1, ey)
        n += self.helper(sx, sy + 1, ex, ey)
        n += self.helper(sx + 1, sy, ex, ey)
        self.table[(sx, sy, ex, ey)] = n
        return n


if __name__ == '__main__':
    print(Solution().countCornerRectangles(
        [[0, 1, 0],
         [1, 0, 1],
         [1, 0, 1],
         [0, 1, 0]]))
