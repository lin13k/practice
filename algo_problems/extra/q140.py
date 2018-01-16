class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {len(s): ['']}

        def breaking(i):
            tmpLt = []
            if i not in memo:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        for tail in breaking(j):
                            tmpLt.append(s[i:j] + (tail and ' ' + tail))
                memo[i] = tmpLt
            print(i, memo)
            return memo[i]
        return breaking(0)

if __name__ == '__main__':
    print(Solution().wordBreak('dogsandcat', [
          'dog', 'dogs', 'sand', 'and', 'cat']))
