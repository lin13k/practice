class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        i = 0
        while i < len(ops):
            if ops[i] == '+':
                ops[i] = sum(ops[max(0, i - 2):i])
            elif ops[i] == 'D':
                if i == 0:
                    ops[i] = 0
                else:
                    ops[i] = 2 * ops[i - 1]
            elif ops[i] == 'C':
                ops.pop(i - 1)
                ops.pop(i - 1)
                i -= 1
                continue
            else:
                ops[i] = int(ops[i])
            i += 1
        return sum(ops)


if __name__ == '__main__':
    print(Solution().calPoints(["5", "2", "C", "D", "+"]))
