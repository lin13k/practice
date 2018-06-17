class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        table = [[0 for i in range(len(nums))] for j in range(len(nums))]

        for gap in range(2, len(nums)):
            for i in range(len(nums) - gap):
                j = i + gap
                tmp = 0
                for k in range(i + 1, j):
                    tmp = max(tmp, table[i][k] + table[k][j] + nums[i] * nums[j] * nums[k])
                table[i][j] = tmp
        return table[0][-1]


if __name__ == '__main__':
    print(Solution().maxCoins([1]))
    print(Solution().maxCoins([1, 2, 3]))
    # print(Solution().maxCoins([3, 1, 5, 2]))
