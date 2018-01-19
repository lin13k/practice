class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqTable = []
        for i in range(int(n**0.5) + 1):
            sqTable.append(i * i)
        # print(sqTable)
        stack = [(n, 0)]
        while len(stack) > 0:
            node = stack.pop(0)
            tmpN = node[0]
            cnt = node[1]
            for q in sqTable[::-1]:
                if tmpN - q == 0:
                    return cnt + 1
                elif tmpN - q > 0:
                    stack.append((tmpN - q, cnt + 1))
        return n


if __name__ == '__main__':
    # print(Solution().numSquares(12))
    # print(Solution().numSquares(13))
    # print(Solution().numSquares(16))
    # print(Solution().numSquares(6166))
    # print(Solution().numSquares(60166))
    print(Solution().numSquares(5756))
