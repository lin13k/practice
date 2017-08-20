class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        lowestPos = left

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            biasMid = (mid + lowestPos) % len(nums)
            if nums[biasMid] == target:
                return biasMid
            if nums[biasMid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    print(Solution().search([1, 3], 0))
    print(Solution().search([0, 1, 2, 3], 0))
    print(Solution().search([1], 1))
