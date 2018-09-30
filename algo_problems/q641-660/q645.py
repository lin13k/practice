from collections import Counter


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        c = Counter(nums)
        lack = -1
        duplicated = -1
        for i in range(1, n + 1):
            if c[i] == 0:
                lack = i
            elif c[i] == 2:
                duplicated = i
            if lack != -1 and duplicated != -1:
                break
        return [duplicated, lack]