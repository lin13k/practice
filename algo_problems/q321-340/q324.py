from statistics import median


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        mid = median(nums)
        i = j = 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] > mid:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < mid:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            else:
                j += 1

        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


if __name__ == '__main__':
    Solution().wiggleSort([4, 1, 2, 5, 3])
