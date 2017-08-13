class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        tmpLt = self.nSum(nums, 0, 3)
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
            raise Exception('not enough nums')
        if len(nums) == n:
            return nums
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
    assert(Solution().threeSum(
        [-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
