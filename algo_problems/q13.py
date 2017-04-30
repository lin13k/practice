class Solution(object):
    Symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        previousN = 0
        for i in range(len(s)):
            tmpN = self.valueOfChar(s[i])
            if tmpN > previousN:
                result += tmpN - 2 * previousN
            else:
                result += tmpN
            previousN = tmpN
        return result

    def valueOfChar(self, char=''):
        n = self.Symbol.index(char)
        return 1 * 2**(n // 2) * max(5**((n + 1) // 2), 1)

if __name__ == '__main__':
    assert(Solution().valueOfChar('I') == 1)
    assert(Solution().valueOfChar('D') == 500)
    assert(Solution().valueOfChar('M') == 1000)

    assert(Solution().romanToInt('I') == 1)
    assert(Solution().romanToInt('D') == 500)
    assert(Solution().romanToInt('M') == 1000)

    assert(Solution().romanToInt('III') == 3)
    assert(Solution().romanToInt('CD') == 400)
    assert(Solution().romanToInt('CM') == 900)
    assert(Solution().romanToInt('M') == 1000)
