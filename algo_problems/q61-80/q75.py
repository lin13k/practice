class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        right_bound = len(nums) - 1
        while right_bound>0 and nums[right_bound] == 2:
            right_bound -= 1
        i = 0
        while i < right_bound:
            if nums[i] == 2:
                tmp = nums[right_bound]
                nums[right_bound] = nums[i]
                nums[i] = tmp
                while right_bound>0 and nums[right_bound] == 2:
                    right_bound -= 1
            i += 1

        i = right_bound
        left_bound = 0
        while left_bound<len(nums) and nums[left_bound] == 0:
            left_bound += 1
        while i > left_bound:
            if nums[i] == 0:
                tmp = nums[left_bound]
                nums[left_bound] = nums[i]
                nums[i] = tmp
                while left_bound<len(nums) and nums[left_bound] == 0:
                    left_bound += 1
            i -= 1
        
if __name__ == '__main__':
    Solution().sortColors([0,1,1,2,2,1,0])
    Solution().sortColors([0,0])
    Solution().sortColors([2,2])