class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * (len(s) + 1)
        d[0] = True
        for i in range(len(s)):
            if d[i] is not True:
                continue
            for w in wordDict:
                if len(w) <= len(s) - i and s[i:len(w) + i] == w:
                    d[len(w) + i] = True
        return d[-1]


if __name__ == '__main__':
    print(Solution().wordBreak('abcd', ['a', 'bc', 'd']))
