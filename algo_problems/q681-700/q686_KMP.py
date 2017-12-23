import math


class Solution:
    def buildKMP(self, s):
        result = [0]
        for i in range(1, len(s)):
            j = result[i - 1]
            while j > 0 and s[i] != s[j]:
                j = result[j - 1]
            if s[i] == s[j]:
                result.append(j + 1)
            else:
                result.append(j)
        return result

    def searchByKMP(self, s, w):
        kmpTable = self.buildKMP(s)
        result = []
        j = 0
        for i in range(len(s)):
            while j > 0 and s[i] != w[j]:
                j = kmpTable[j - 1]
            if s[i] == w[j]:
                j += 1
            if j == len(w):
                result.append(i - j + 1)
                j = 0
        return result

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        """
        case 1
        if B in A*(math.ceil(len(B)/len(A)))
            return math.ceil(len(B)/len(A))
        case 2
        if B in A*(math.ceil(len(B)/len(A))+1)
            return math.ceil(len(B)/len(A))+1
        return -1
        """
        if len(B) == 0:
            return 1
        if len(A) == 0:
            return -1
        repeatNumber = math.ceil(len(B) / len(A))
        if len(self.searchByKMP(A * repeatNumber, B)) > 0:
            return repeatNumber
        if len(self.searchByKMP(A * (repeatNumber + 1), B)) > 0:
            return repeatNumber + 1
        return -1
