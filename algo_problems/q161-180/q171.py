class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        result = 0
        n = len(s)
        for i in range(n):
            result += (ord(s[i]) - 64) * (26**(n - i - 1))
        return result


if __name__ == '__main__':
    print(Solution().titleToNumber('AA'))
    print(Solution().titleToNumber('AC'))
    print(Solution().titleToNumber('ACB'))
