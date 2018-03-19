from collections import Counter


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = Counter(s)
        oddCount = 0
        for k in d:
            if d[k] & 1:
                oddCount += 1
        return oddCount < 2


if __name__ == '__main__':
    print(Solution().canPermutePalindrome('abcb'))
    print(Solution().canPermutePalindrome('aba'))
    print(Solution().canPermutePalindrome('abc'))
    print(Solution().canPermutePalindrome('abcb'))