class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sIdx = 0
        pIdx = 0
        starIdx = None
        backMatchIdx = 0
        while sIdx < len(s):
            if pIdx < len(p) and (p[pIdx] == '?' or s[sIdx] == p[pIdx]):
                sIdx += 1
                pIdx += 1
                continue
            elif pIdx < len(p) and p[pIdx] == '*':
                starIdx = pIdx
                pIdx += 1
                backMatchIdx = sIdx
                continue
            elif starIdx is not None:
                backMatchIdx += 1
                sIdx = backMatchIdx
                pIdx = starIdx + 1
                continue
            return False

        while pIdx < len(p) and p[pIdx] == '*':
            pIdx += 1
        return pIdx == len(p)

if __name__ == '__main__':
    print(Solution().isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"))
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa", "*"))


