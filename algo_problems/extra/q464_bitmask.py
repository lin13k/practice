class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= 0 or maxChoosableInteger >= desiredTotal:
            return True
        maxsum = maxChoosableInteger * (maxChoosableInteger + 1) / 2
        if maxsum == desiredTotal:
            return maxChoosableInteger % 2 == 1
        if maxsum < desiredTotal:
            return False
        self.table = {}
        bitmask = 1 << maxChoosableInteger
        return self.helper(maxChoosableInteger, bitmask, desiredTotal)

    def helper(self, m, bitmask, desiredTotal):
        if bitmask in self.table:
            return self.table[bitmask]
        for i in range(m):
            if (1 & (bitmask >> i)):
                continue
            n = i + 1
            if (n >= desiredTotal) or (self.helper(m, bitmask | (1 << i), desiredTotal - n) is False):
                self.table[bitmask] = True
                return True
        self.table[bitmask] = False
        return False
