class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                tmp = len(result)
            for j in range(len(result) - tmp, len(result)):
                result.append(result[j] + [nums[i]])
        return result

if __name__ == '__main__':
    print(Solution().subsetsWithDup([1]))
    print(Solution().subsetsWithDup([1, 2]))
    print(Solution().subsetsWithDup([1, 2, 2]))
