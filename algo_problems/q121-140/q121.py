class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        profits = [0]
        maxPrice = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            profits.append(maxPrice - prices[i])
            if prices[i] > maxPrice:
                maxPrice = prices[i]
        return max(profits)
