class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [[1, 1] for i in range(10)]

        for i in range(N - 1):
            for j in range(10):
                if j == 5:
                    continue
                if j == 0:
                    dp[j][(i + 1) % 2] = (dp[4][i % 2] + dp[6][i % 2])
                if j == 1:
                    dp[j][(i + 1) % 2] = (dp[6][i % 2] + dp[8][i % 2])
                if j == 2:
                    dp[j][(i + 1) % 2] = (dp[7][i % 2] + dp[9][i % 2])
                if j == 3:
                    dp[j][(i + 1) % 2] = (dp[4][i % 2] + dp[8][i % 2])
                if j == 4:
                    dp[j][(i + 1) % 2] = (dp[0][i % 2] +
                                          dp[3][i % 2] + dp[9][i % 2])
                if j == 6:
                    dp[j][(i + 1) % 2] = (dp[0][i % 2] +
                                          dp[1][i % 2] + dp[7][i % 2])
                if j == 7:
                    dp[j][(i + 1) % 2] = (dp[2][i % 2] + dp[6][i % 2])
                if j == 8:
                    dp[j][(i + 1) % 2] = (dp[1][i % 2] + dp[3][i % 2])
                if j == 9:
                    dp[j][(i + 1) % 2] = (dp[2][i % 2] + dp[4][i % 2])

        result = max(sum([dp[i][0] for i in range(10)]),
                     sum([dp[i][1] for i in range(10)]))
        if N == 1:
            return result
        else:
            return (result - 1) % (10**9 + 7)


if __name__ == '__main__':
    print(Solution().knightDialer(4904))
