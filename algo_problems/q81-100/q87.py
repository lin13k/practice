class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.recursiveCheck(s1, s2)

    def recursiveCheck(self, s1, s2):
        # print(s1, s2)

        if s1 == s2:
            return True
        n = len(s1)
        if n != len(s2):
            return False
        if n == 1 and s1 != s2:
            return False

        result = False

        for i in range(1, len(s1)):
            result = result or (self.recursiveCheck(s1[:i], s2[n - i:]) and
                                self.recursiveCheck(s1[i:], s2[:n - i]))
            if result:
                return result
            result = result or (self.recursiveCheck(s1[:i], s2[:i]) and
                                self.recursiveCheck(s1[i:], s2[i:]))
            if result:
                return result
        return result


if __name__ == '__main__':
    # print(Solution().isScramble('abc', 'abc'))
    # print(Solution().isScramble('abc', 'cab'))
    # print(Solution().isScramble('cab', 'abc'))
    # print(Solution().isScramble('cba', 'abc'))
    # print(Solution().isScramble('acc', 'abc'))
    # print(Solution().isScramble('abb', 'bab'))
    # print(Solution().isScramble('abc', 'bac'))
    # print(Solution().isScramble('ab', 'aa'))
    print(Solution().isScramble('abcdefghijklmnopq', 'efghijklmnopqcadb'))
