class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dpList = [1, 1]

        for i in range(2, n + 1):
            dpList.append(dpList[i - 2] + dpList[i - 1])
        return dpList[n]


if __name__ == '__main__':
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))
    print(Solution().climbStairs(5))