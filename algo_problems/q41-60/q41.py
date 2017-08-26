class Solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                tmpIndex = nums[i] - 1
                nums[i], nums[tmpIndex] = nums[tmpIndex], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([1, 2, 3]))
    print(Solution().firstMissingPositive([1, 2, 1, 1, 2, 0]))
    print(Solution().firstMissingPositive([1, 2, 2, 2, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, 1, 0]))
    print(Solution().firstMissingPositive([3, 4, -1]))
