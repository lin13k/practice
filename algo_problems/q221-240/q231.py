class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hDistance = 0
        while n > 0:
            if n & 1 == 1:
                hDistance += 1
            n >>= 1
        return hDistance == 1

if __name__ == '__main__':
    print(Solution().isPowerOfTwo(1))
    print(Solution().isPowerOfTwo(12))
    print(Solution().isPowerOfTwo(16))
    print(Solution().isPowerOfTwo(4))
    print(Solution().isPowerOfTwo(1024))