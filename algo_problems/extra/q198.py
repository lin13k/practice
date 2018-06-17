import sys
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        table = [0 for j in range(len(nums))]
        for i in range(n):
            if i -2 >= 0:
                premax = table[i - 2]
            else:
                premax = 0
            table[i] = max(table[i - 1], nums[i] + premax)
        print(table)
        return table[-1] if len(table) > 0 else 0

if __name__ == '__main__':
    print(Solution().rob([2,1,1,2]))