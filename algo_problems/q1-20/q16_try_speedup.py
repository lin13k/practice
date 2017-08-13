class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        return self.nSumClosest(nums, target, 3)

    def nSumClosest(self, nums, target, n):
        if len(nums) < n:
            raise Exception('not enough nums')
        if len(nums) == n:
            return sum(nums)
        if n == 2:
            return self.twoSumClosest(nums, target)
        else:
            tmpResult = []
            for i in range(len(nums) - n + 1):
                tmpResult.append(
                    nums[i] + self.nSumClosest(
                        nums[i + 1:], target - nums[i], n - 1))
                if target in tmpResult:
                    return target
            closestN = tmpResult[0]
            for i in tmpResult:
                if abs(closestN - target) > abs(i - target):
                    closestN = i
            return closestN

    def twoSumClosest(self, nums, target):
        i = 0
        j = len(nums) - 1
        tmp = nums[i] + nums[j]
        while i < j:
            if abs(tmp - target) > abs(nums[i] + nums[j] - target):
                tmp = nums[i] + nums[j]
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return tmp
        return tmp


if __name__ == '__main__':
    # print(Solution().twoSumClosest([1, 2, 3, 4, 5, 6], 12))
    # print(Solution().twoSumClosest([1, 2, 3, 4, 5, 6], 7))
    # print(Solution().twoSumClosest([1, 2, 3, 4, 5, 6], 7))
    # print(Solution().nSumClosest([1, 2, 3, 4, 5, 6], 16, 3))
    print(Solution().threeSumClosest([1, 1, 1, 0], 100))
