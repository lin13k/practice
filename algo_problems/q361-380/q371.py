class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        while a:
            a, b = ((a & b) << 1), (a ^ b)
            a &= 0xFFFFFFFF
            b &= 0xFFFFFFFF

        signed = (1 << 31) & b
        if signed:
            return ~(b ^ 0xFFFFFFFF)
        else:
            return b


if __name__ == '__main__':
    # print(Solution().getSum(5, 7))
    print(Solution().getSum(-1, -7))
