class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        r = nums[0]
        cmax = r
        cmin = r
        for num in nums[1:]:
            if num < 0:
                cmax, cmin = cmin, cmax
            cmax = max(num, cmax * num)
            cmin = min(num, cmin * num)
            r = max(r, cmax)
        return r


if __name__ == '__main__':
    print(Solution().maxProduct([1, 2, 3]))
    print(Solution().maxProduct([1, 2, -3]))
    print(Solution().maxProduct([1, 0, -3, -1]))
    print(Solution().maxProduct([-2]))
