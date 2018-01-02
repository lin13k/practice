class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        previousNum = None
        count = 0
        result = 0

        i = 0
        while i < len(nums):
            if previousNum != nums[i]:
                previousNum = nums[i]
                count = 0
                result += 1
            else:
                count += 1
                if count > 1:
                    nums.pop(i)
                    continue
                else:
                    result += 1
            i += 1

        return result

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,1,2,2,3,3,3,4]))