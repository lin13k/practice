class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        hashDict = {}
        self.recursiveFindSubset(sorted(nums), [], hashDict)

        for i in hashDict:
            result.append(list(i))
        return result

    def recursiveFindSubset(self, nums, path, result):
        if len(nums) == 0:
            result[(*path,)] = 1
            return
        self.recursiveFindSubset(nums[1:], path + [nums[0]], result)
        self.recursiveFindSubset(nums[1:], path, result)


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1]))
    print(Solution().subsetsWithDup([1, 2]))
    print(Solution().subsetsWithDup([1, 2, 2]))
