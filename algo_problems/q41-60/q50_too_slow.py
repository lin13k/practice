class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if abs(x) == 1:
            return -1 if x < 0 and n % 2 == 1 else 1
        result = 1
        sign = True if x < 0 else False
        x = abs(x) if n > 0 else (1 / abs(x))
        i = 0
        while i < abs(n):
            result *= x
            if result < 1.175494e-38:
                return 1.175494e-38
            elif result > 3.402823e+38:
                return 3.402823e+38
            i += 1
        if sign and n % 2 == 1:
            return - result
        return result


if __name__ == '__main__':
    print(Solution().myPow(-13.62608, 3))
