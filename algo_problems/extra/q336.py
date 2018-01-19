class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        wDict = {}
        for i in range(len(words)):
            wDict[words[i]] = i

        if '' in wDict:
            for i in range(len(words)):
                if i != wDict[''] and self.isPalindrome(words[i]):
                    result.append([i, wDict['']])
                    result.append([wDict[''], i])

        for w in words:
            if w[::-1] in wDict and wDict[w] != wDict[w[::-1]]:
                result.append([wDict[w], wDict[w[::-1]]])

        for w in words:
            for j in range(1, len(w)):
                if self.isPalindrome(w[j:]) and w[:j][::-1] in wDict:
                    result.append([wDict[w], wDict[w[:j][::-1]]])
            for j in range(1, len(w)):
                if self.isPalindrome(w[:j]) and w[j:][::-1] in wDict:
                    result.append([wDict[w[j:][::-1]], wDict[w]])

        return result

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    print(Solution().palindromePairs(['abc', 'ba', 'cba', 'a']))
