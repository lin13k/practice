class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        tank = 0
        start = 0
        total = 0
        for i in range(n):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                total += tank
                tank = 0
                start = i + 1

        if tank + total < 0:
            return -1
        else:
            return start


if __name__ == '__main__':
    # print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [2, 1, 3, 4, 5]))
    print(Solution().canCompleteCircuit([1, 2, 3, 4, 3, 2, 4, 1, 5, 3, 2, 4],
                                        [1, 1, 1, 3, 2, 4, 3, 6, 7, 4, 3, 1]))
