class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        Symbol  I   V   X   L   C   D   M
        Value   1   5   10  50  100 500 1,000
        """
        Symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        result = []
        tmpN = num
        for i in range(3, -1, -1):
            digit = self.getDigit(tmpN, i)
            if digit == 0:
                continue
            elif digit == 1:
                result += Symbol[i * 2]
            elif digit == 2:
                result += Symbol[i * 2] * 2
            elif digit == 3:
                result += Symbol[i * 2] * 3
            elif digit == 4:
                result += Symbol[i * 2] + Symbol[i * 2 + 1]
            elif digit == 5:
                result += Symbol[i * 2 + 1]
            elif digit == 6:
                result += Symbol[i * 2 + 1] + Symbol[i * 2]
            elif digit == 7:
                result += Symbol[i * 2 + 1] + Symbol[i * 2] * 2
            elif digit == 8:
                result += Symbol[i * 2 + 1] + Symbol[i * 2] * 3
            else:
                result += Symbol[i * 2] + Symbol[i * 2 + 2]
        return ''.join(result)

    def getDigit(self, n, digit):
        return (n % 10**(digit + 1)) // (10**digit)

if __name__ == '__main__':
    # assert(Solution().getDigit(12345, 0)==5)
    # assert(Solution().getDigit(12345, 1)==4)
    # assert(Solution().getDigit(12345, 2)==3)
    # assert(Solution().getDigit(12345, 3)==2)
    # assert(Solution().getDigit(12345, 4)==1)

    print(Solution().intToRoman(1))
    print(Solution().intToRoman(11))
    print(Solution().intToRoman(15))
    print(Solution().intToRoman(17))
    print(Solution().intToRoman(18))
    print(Solution().intToRoman(19))
