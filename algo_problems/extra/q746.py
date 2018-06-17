class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        table = [[0 for j in range(2)] for i in range(n + 1)]

        for i in range(n):
            table[i + 1][0] = min(table[i][0] + cost[i], table[i][1])
            table[i + 1][1] = min(table[i][0] + cost[i], table[i][1] + cost[i])
        return min(table[-1])


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([10, 15, 20]))
    print(Solution().minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
