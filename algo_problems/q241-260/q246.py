class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range((n + 1) // 2):
            c = num[i]
            d = num[n - 1 - i]
            if c in '018' and c == d:
                continue
            if c in '69' and d in '69' and c != d:
                continue
            return False
        return True


if __name__ == '__main__':
    print(Solution().isStrobogrammatic('11811'))
    print(Solution().isStrobogrammatic('1811'))
    print(Solution().isStrobogrammatic('1691'))
    print(Solution().isStrobogrammatic('16191'))
