class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        for i in range(n - 2, -1, -1):
            row = triangle[i]
            for j in range(len(row)):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__ == '__main__':
    print(Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
