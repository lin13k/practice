class Solution(object):
    def threeSum(self, nums):
        result = {}
        if nums.count(0) > 2:
            result[(0, 0, 0)] = 1
        nums = self.preprocess(nums)
        nums.sort()
        N = len(nums)
        for i in range(N - 2):
            tmpN1 = -nums[i]
            j = i + 1
            k = N - 1
            while j < k:
                if nums[j] + nums[k] == tmpN1:
                    result[(nums[i], nums[j], nums[k])] = 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < tmpN1:
                    j += 1
                else:
                    k -= 1

        return list(map(list, result.keys()))

    def preprocess(self, nums):
        from collections import Counter
        d = Counter(nums)
        result = []
        for k, v in d.items():
            result += [k] * min(2, v)
        return result

if __name__ == '__main__':
    assert(Solution().threeSum(
        [-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
