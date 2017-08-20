class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lowerLimit = self.findLowerLimit(nums, target)
        if nums[lowerLimit] < target:
            return lowerLimit + 1
        return lowerLimit

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
    print(Solution().findUpperLimit([0, 1, 1, 1, 2, 2, 3], 1))
    print(Solution().findLowerLimit([0, 1, 1, 1, 2, 2, 3], 1))

    print(Solution().findUpperLimit([0, 0, 0, 0, 1, 1, 1, 2, 2, 3], 1))
    print(Solution().findLowerLimit([0, 0, 0, 0, 1, 1, 1, 2, 2, 3], 1))
