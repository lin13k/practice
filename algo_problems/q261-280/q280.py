class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if (i & 1 and nums[i + 1] > nums[i]) or (not i & 1 and nums[i + 1] < nums[i]):
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
        print(nums)


# 1,2,3,4,5
# 1,3,2,5,4
if __name__ == '__main__':
    Solution().wiggleSort([1, 2, 3])
    Solution().wiggleSort([1, 2, 3, 4])
    Solution().wiggleSort([1, 2, 3, 4, 5, 6])
    # Solution().wiggleSort([1, 2, 3, 4, 5])
    # Solution().wiggleSort([1, 2, 3, 4, 5, 6, 7])
    # Solution().wiggleSort([1, 2])
    #
