class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        if n != 1:
            for i in range(n - 1):
                result = self.genStr(result)
        return result
        
    def genStr(self, s):
        c = s[0]
        i = 1
        ancher = 0
        result = ''
        while i < len(s):
            if s[i] != c:
                result += str(i - ancher) + c
                ancher = i
                c = s[i]
            i += 1

        if ancher != i:
            result += str(i - ancher) + c

        return result

if __name__ == '__main__':
    print(Solution().countAndSay(1))
    print(Solution().countAndSay(2))
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))
    print(Solution().countAndSay(6))

    # print(Solution().genStr('11'))
    # print(Solution().genStr('1122'))
    # print(Solution().genStr('1133123'))
    # print(Solution().genStr('114421'))
