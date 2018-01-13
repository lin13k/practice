class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # m = 4
        # n = 6
        # 000111
        # 001110
        # 000101
        # 001000
        #
        m = len(M)
        if m == 0:
            return 0
        n = len(M[0])
        if n == 0:
            return 0

        maxInt = 0
        for i in range(m):
            count = 0
            for j in range(n):
                if M[i][j] == 0:
                    count = 0
                else:
                    count += 1
                    maxInt = max(maxInt, count)
        for j in range(n):
            count = 0
            for i in range(m):
                if M[i][j] == 0:
                    count = 0
                else:
                    count += 1
                    maxInt = max(maxInt, count)

        if maxInt == m or maxInt == n:
            return maxInt
        for i in range(-m + 1, m):
            count = 0
            for j in range(n - 1, -1, -1):
                if j + i < 0:
                    break
                if j + i >= m:
                    continue
                if M[i + j][j] == 0:
                    count = 0
                else:
                    count += 1
                    maxInt = max(maxInt, count)
            count = 0
            for j in range(n):
                if i + n - j - 1 < 0:
                    break
                if i + n - j - 1 >= m:
                    continue
                if M[i + n - j - 1][j] == 0:
                    count = 0
                else:
                    count += 1
                    maxInt = max(maxInt, count)
        return maxInt


if __name__ == '__main__':
    print(Solution().longestLine([
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]))

    print(Solution().longestLine([
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]))
