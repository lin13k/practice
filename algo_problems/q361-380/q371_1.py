class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while a:
            a = (a & b << 1)
            b = a | b
            a &= 0xffffffff
            b &= 0xffffffff

        signed = (1 << 31) & b
        if signed:
            return ~(b ^ 0xffffffff)
        else:
            return b