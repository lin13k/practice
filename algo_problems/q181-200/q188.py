class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or prices is None or len(prices) == 0:
            return 0
        if k >= len(prices) / 2:
            lt = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)
                  if prices[i] < prices[i + 1]]
            return sum(lt)

        table = [[0 for j in range(k + 1)] for i in range(len(prices))]

        for j in range(1, k + 1):
            localMax = 0
            for i in range(1, len(prices)):
                profit = prices[i] - prices[i - 1]
                localMax = max(
                    table[i - 1][j - 1] + profit,
                    table[i - 1][j - 1],
                    localMax
                )
                table[i][j] = max(table[i - 1][j], localMax)

        print('\n'.join(map(str, table)))
        return table[len(prices) - 1][k]


if __name__ == '__main__':
    # print(Solution().maxProfit(3, [1, 2, 1, 2, 1, 2, 1, 2]))
    # print(Solution().maxProfit(2, [4, 2, 3]))
    # print(Solution().maxProfit(1, [1, 1, 0, 1, 1, 1]))
    print(Solution().maxProfit(1, [1, 4, 2, 3, 5]))
    print(Solution().maxProfit(2, [1, 4, 2, 3, 5]))
