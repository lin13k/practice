class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0
        tmpSum = nums[0] + nums[1] + nums[2]
        tmpTarget = tmpSum
        for i in range(3, len(nums)):
            tmpSum = tmpSum + nums[i] - nums[i - 3]
            if abs(tmpSum - target) < abs(tmpTarget - target):
                tmpTarget = tmpSum
        return tmpTarget


if __name__ == '__main__':
    assert(Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2)
    assert(Solution().threeSumClosest([-1, 2, 1, -4, 4], 1) == 1)
    assert(Solution().threeSumClosest([-1, 2, 1, -4, 4, 3], 3) == 3)
