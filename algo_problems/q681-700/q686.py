import math


class Solution:
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
        if B in A * (math.ceil(len(B) / len(A))):
            return math.ceil(len(B) / len(A))
        if B in A * (math.ceil(len(B) / len(A)) + 1):
            return math.ceil(len(B) / len(A)) + 1
        return -1
