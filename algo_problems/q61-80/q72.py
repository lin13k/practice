class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        n1 = len(word1)
        n2 = len(word2)
        dpTable = [[i + j for i in range(n2 + 1)] for j in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dpTable[i][j] = dpTable[i - 1][j - 1]
                else:
                    dpTable[i][j] = min(dpTable[i - 1][j - 1],
                                        dpTable[i - 1][j],
                                        dpTable[i][j - 1]) + 1

        print(dpTable)
        return dpTable[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance('abcd', 'aabb'))
    # print(Solution().minDistance('abcdaabb', 'aabb'))
    # print(Solution().minDistance('a', 'ab'))
    # print(Solution().minDistance('a', 'a'))
