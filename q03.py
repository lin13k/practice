from collections import Counter
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = s + s[::-1]
        d = {}
        maxInt = 1
        n = len(s)
        for i in range(n):
            if s[i] in d:
                maxInt = max(maxInt, i - d[s[i]], i - sorted(list(d.values()))[0])
                d = {}
            d[s[i]] = i
        maxInt = max(maxInt, n - sorted(list(d.values()))[0])
        return maxInt

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("asjrgapa"))