class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.search(nums, [], result)
        return result

    def search(self, nums, path, result):
        if len(nums) == 1:
            result.append(path + nums)
        else:
            for i in range(len(nums)):
                self.search(nums[0:i] + nums[i + 1:], path + [nums[i]], result)


if __name__ == '__main__':
    # print(Solution().permute([1,2,3]))
    print(Solution().permute([1, 2, 3, 4]))
