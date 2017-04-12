class Solution(object):

    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        lastIndex = 0
        maxInt = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                lastIndex = max(d[s[i]] + 1, lastIndex)
            d[s[i]] = i
            maxInt = max(maxInt, i - lastIndex)
        return maxInt + 1

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
    print(Solution().lengthOfLongestSubstring("asjrgapa"), 6)
    print(Solution().lengthOfLongestSubstring("abc"), 3)
    print(Solution().lengthOfLongestSubstring("jxdlnaiaij"), 7)
    print(Solution().lengthOfLongestSubstring("a"), 1)
    print(Solution().lengthOfLongestSubstring("aa"), 1)
    print(Solution().lengthOfLongestSubstring("aaa"), 1)
    print(Solution().lengthOfLongestSubstring("caa"), 2)
    print(Solution().lengthOfLongestSubstring("tmmzuxt"), 5)
