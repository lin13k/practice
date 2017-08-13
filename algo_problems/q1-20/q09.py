class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = len(str(x))
        for i in range(n // 2):
            rightDigit = x % 10**(i + 1) // 10**(i)
            leftDigit = (x % 10**(n - i)) // 10**(n - i - 1)
            if rightDigit != leftDigit:
                return False
        return True
