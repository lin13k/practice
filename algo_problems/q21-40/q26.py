class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return nums

if __name__ == '__main__':
    print(Solution().removeDuplicates([]))
    print(Solution().removeDuplicates([1, 1, 2, 2, 3, 3]))
    print(Solution().removeDuplicates([1, 2, 3, 4, 4, 4, 5, 5, 5]))
