class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().numDistinct('rabbbit', 'rabbit'))
    print(Solution().numDistinct('babgbag', 'bag'))
