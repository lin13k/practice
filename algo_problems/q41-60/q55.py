class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            False
        currentLimit = nums[0]
        i = 0
        while i <= currentLimit and i < len(nums):
            currentLimit = max(currentLimit, i + nums[i])
            i += 1

        return i == len(nums)


if __name__ == '__main__':
    print(Solution().canJump([2,3,1,1,4]))
    print(Solution().canJump([3,2,1,0,4]))
