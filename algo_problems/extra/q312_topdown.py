class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        table = [[0 for i in range(len(nums))] for j in range(len(nums))]

        def helper(s, e):
            if table[s][e] or e <= s + 1:
                return table[s][e]
            tmp = 0
            for i in range(s + 1, e):
                tmp = max(tmp, nums[s] * nums[i] * nums[e] +
                          helper(s, i) + helper(i, e))
            table[s][e] = tmp
            return tmp
        helper(0, len(nums) - 1)
        print(table)
        return table[0][-1]

if __name__ == '__main__':
    print(Solution().maxCoins([1]))
    # print(Solution().maxCoins([1, 2, 3]))
    # print(Solution().maxCoins([3, 1, 5, 2]))
