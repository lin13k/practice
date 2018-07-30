class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        for length in range(1, 6):

            for root in range(int(10**(length - 1)), int(10**(length))):
                tmpS = str(root)
                testN = int(tmpS + tmpS[-2::-1])
                if testN >= N:
                    if self.isPrime(testN):
                        return testN
            for root in range(int(10**(length - 1)), int(10**(length))):
                tmpS = str(root)
                testN = int(tmpS + tmpS[::-1])
                if testN >= N:
                    if self.isPrime(testN):
                        return testN

    def isPrime(self, n):
        return n > 1 and all(n%d for d in range(2, int(n**0.5) + 1))


if __name__ == '__main__':
    print(Solution().primePalindrome(8))
    print(Solution().primePalindrome(1))
    print(Solution().primePalindrome(2))
    print(Solution().primePalindrome(4))
    print(Solution().primePalindrome(7))
    print(Solution().primePalindrome(930))
    # print(Solution().primePalindrome(12))
    print(Solution().primePalindrome(13))
