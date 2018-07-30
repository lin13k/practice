class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0

        def helper(i, j, triangle):
            if i >= len(triangle) - 1:
                return triangle[i][j]
            return triangle[i][j] + min(
                helper(i + 1, j, triangle),
                helper(i + 1, j + 1, triangle))
        return helper(0, 0, triangle)


if __name__ == '__main__':
    print(Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
