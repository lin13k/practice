from math import ceil


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxN = max(nums)
        minN = min(nums)
        n = len(nums)

        buckSize = (maxN - minN) // (n - 1)
        buckNum = ceil((maxN - minN) / (buckSize))

        bucks = [[maxN, minN] for i in range(buckNum)]
        for num in nums:

