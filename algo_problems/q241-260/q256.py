class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        n = len(costs)
        if n < 1:
            return 0
        table = [[0 for j in range(3)] for i in range(n + 1)]

        for i in range(n):
            for j in range(3):
                table[i + 1][j] = min(
                    table[i][j - 1] + costs[i][j],
                    table[i][j - 2] + costs[i][j])
        return min(table[-1])
