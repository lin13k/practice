class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.getPowerSets(nums, [], result)
        return result

    def getPowerSets(self, nums, previous, result):

        if len(nums) == 0:
            result.append(previous)
            return

        self.getPowerSets(nums[1:], previous + [nums[0]], result)
        self.getPowerSets(nums[1:], previous, result)


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3, 4]))
