from collections import defaultdict


class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c = defaultdict(int)
        start = end = 0
        n = len(s)
        maxCnt = 0
        while end < n:
            c[s[end]] += 1
            maxCnt = max(c[s[end]], maxCnt)
            while end - start + 1 - maxCnt > k:
                c[s[start]] -= 1
                start += 1
            end += 1
        return end - start


if __name__ == '__main__':
    print(Solution().characterReplacement('ABAB', 2))
    print(Solution().characterReplacement('ABACAB', 2))
