class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = {}
        for i in nums:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1

        m = 0
        n = None

        for i in c:
            if c[i] > m:
                n = i
                m = c[i]
        return n
