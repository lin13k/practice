from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        a = Counter(s1)
        print('a', a)
        winSize = len(s1)
        b = Counter(s2[:winSize - 1])
        print('b', b)
        for i in range(winSize - 1, len(s2)):
            b[s2[i]] += 1
            if a == b:
                return True
            b[s2[i - winSize + 1]] -= 1
            if b[s2[i - winSize + 1]] == 0:
                del b[s2[i - winSize + 1]]
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion('ab', 'bdca'))
    print(Solution().checkInclusion('ab', 'bdcab'))
