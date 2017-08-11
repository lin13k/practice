class Solution(object):
    def threeSumClosest(self, nums, target):
        pass

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
            for i in range(len(nums) - n):
                tmpLt = self.nSum(nums[i + 1:], target - nums[i], n - 1)
                solutions = [(nums[i],) + item for item in tmpLt]
                tmpResult.extend(solutions)
            return tmpResult

    def twoSumCloset(self, nums, target):
        i = 0
        j = len(nums) - 1
        tmp = nums[i] + nums[j]
        tmpIdx = (i, j)
        while i < j:
            if abs(tmp - target) > abs(nums[i] + nums[j] - target):
                tmp = nums[i] + nums[j]
                tmpIdx = (i, j)
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return (nums[tmpIdx[0]], nums[tmpIdx[1]])


if __name__ == '__main__':
    print(Solution().nSum([1, 2, 3, 4, 5, 6], 7, 2))
    print(Solution().nSum([1, 2, 3, 4, 5, 6], 7, 3))
    print(Solution().nSum([1, 2, 3, 4, 5, 6], 7, 4))
