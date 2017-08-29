class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if abs(x) == 1:
            return -1 if x < 0 and n % 2 == 1 else 1
        elif n == 0:
            return 1
        result = x if n > 0 else 1 / x
        x = x if n > 0 else 1 / x
        dummy = 1
        n = abs(n)
        while n > 1:
            if n % 2 == 1:
                n -= 1
                dummy *= result
            result = result * result
            n = n // 2
        return result * dummy


if __name__ == '__main__':
    print(Solution().myPow(2, 3))
    print(Solution().myPow(2, -3))
    print(Solution().myPow(2, 4))
    print(Solution().myPow(2, 5))
    print(Solution().myPow(2, 6))
    print(Solution().myPow(2, -6))
    print(Solution().myPow(-2, 5))
    print(Solution().myPow(-2, -2))
    print(Solution().myPow(34.00515, -3))
    print(Solution().myPow(4.70975, -6))
