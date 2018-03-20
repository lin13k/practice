from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        c = Counter(nums)
        for key in c:
            if c[key] == 1:
                result.append(key)

        return result