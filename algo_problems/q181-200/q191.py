class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            result += n & 1
            n >>= 1
        return result


if __name__ == '__main__':
    print(Solution().hammingWeight(1))
    print(Solution().hammingWeight(2))
    print(Solution().hammingWeight(3))
    print(Solution().hammingWeight(4))
    print(Solution().hammingWeight(18))
