from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cc = Counter(s)
        for i in range(len(s)):
            if cc[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar('abccbaef'))
