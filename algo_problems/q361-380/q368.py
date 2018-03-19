class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        subsets = {}
        maxLen = 0
        result = []
        for i in nums:
            is_grouped = False
            for j in nums:
                if i == j:
                    continue
                if i % j == 0:
                    subsets[i] = subsets[j] + [i]
                    is_grouped = True
                    if len(subsets[i]) > maxLen:
                        maxLen = len(subsets[i])
                        result = subsets[i]
            if not is_grouped:
                subsets[i] = [i]
                if len(subsets[i]) > maxLen:
                    maxLen = len(subsets[i])
                    result = subsets[i]
        return result


if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([1, 2, 3, 4]))
