class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        result = 0
        for i in range(32):
            if n >> i & 1 == 1:
                result += 1 << (31 - i)

        return result


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
