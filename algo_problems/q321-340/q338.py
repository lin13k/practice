class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 0:
            return []
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]

        table = [0 for i in range(num + 1)]
        table[1] = 1
        maxBit = 1
        for i in range(2, len(table)):
            if i == maxBit << 1:
                maxBit = maxBit << 1
            table[i] = table[i - maxBit] + 1
        return table


if __name__ == '__main__':
    print(Solution().countBits(20))
