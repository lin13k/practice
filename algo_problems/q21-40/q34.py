class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lowerLimit = self.findLowerLimit(nums, target)
        if len(nums) == 0 or nums[lowerLimit] != target:
            return [-1, -1]
        return [lowerLimit, self.findUpperLimit(nums, target)]

    def findUpperLimit(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return right

    def findLowerLimit(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    print(Solution().findUpperLimit([0,1,1,1,2,2,3], 1))
    print(Solution().findLowerLimit([0,1,1,1,2,2,3], 1))

    print(Solution().findUpperLimit([0,0,0,0,1,1,1,2,2,3], 1))
    print(Solution().findLowerLimit([0,0,0,0,1,1,1,2,2,3], 1))