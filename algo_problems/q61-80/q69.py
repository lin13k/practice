class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x
        while n * n > x:
            n = (n + x / n) / 2
        return n
