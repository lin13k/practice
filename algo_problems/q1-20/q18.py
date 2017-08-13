class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        tmpLt = self.nSum(nums, target, 4)
        tmpKeys = dict.fromkeys(tmpLt).keys()
        return [list(item) for item in tmpKeys]

    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        result = []
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                result.append((nums[i], nums[j]))
                j -= 1
                i += 1
        return result

    def nSum(self, nums, target, n):
        if len(nums) < n:
            return []
        if len(nums) == n:
            if sum(nums)== target:
                return [tuple(nums)]
            else:
                return []
        if n == 2:
            return self.twoSum(nums, target)
        else:
            tmpResult = []
            for i in range(len(nums) - n + 1):
                tmpLt = self.nSum(nums[i + 1:], target - nums[i], n - 1)
                solutions = [(nums[i],) + item for item in tmpLt]
                tmpResult.extend(solutions)
            return tmpResult


if __name__ == '__main__':
    # print(Solution().fourSum([0], 0))
    # print(Solution().fourSum([], 0))
    # print(Solution().fourSum([0,0,0,0], 1))
    # print(Solution().fourSum([0,0,0,0], 0))
    print(Solution().fourSum([-1,0,1,2,-1,-4], -1))