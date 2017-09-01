class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        accumulatedValue = nums[0]
        globalMax = nums[0]
        for i in range(1, len(nums)):
            accumulatedValue = max(accumulatedValue + nums[i], nums[i])
            globalMax = max(globalMax, accumulatedValue)

        return globalMax
