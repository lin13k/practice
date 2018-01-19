class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        # print(nums)
        return result


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4, 2, 3, 6, 7, 1, 1]))
    print(Solution().findDisappearedNumbers([2, 2]))
