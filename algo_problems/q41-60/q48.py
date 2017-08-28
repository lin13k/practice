class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        checkScopeI = (n + 1) // 2
        checkScopeJ = checkScopeI if n % 2 == 0 else checkScopeI - 1

        m = n - 1
        for i in range(checkScopeI):
            for j in range(checkScopeJ):
                matrix[i][j], matrix[m - j][i], matrix[m - i][m - j], matrix[j][m - i] = \
                matrix[m - j][i], matrix[m - i][m - j], matrix[j][m - i], matrix[i][j]


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(a)
    print(a)

    a = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(a)
    print(a)

