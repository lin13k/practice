class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        tmpStr = str(x)
        n = len(tmpStr)
        for i in range(n // 2):
            if tmpStr[i] != tmpStr[n - i - 1]:
                return False

        return True
