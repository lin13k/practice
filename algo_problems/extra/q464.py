class Solution(object):

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # init dp table
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        table = {}

        self.used = [False for i in range(maxChoosableInteger + 1)]
        return self.helper(table, desiredTotal)

    def helper(self, table, desiredTotal):

        if desiredTotal <= 0:
            return False
        key = tuple(self.used)
        if key not in table:

            for i in range(1, len(self.used)):
                if self.used[i]:
                    continue
                self.used[i] = True

                if not self.helper(table, desiredTotal - i):
                    table[key] = True
                    self.used[i] = False
                    return True

                self.used[i] = False
            table[key] = False

        return table[key]
