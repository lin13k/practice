import math


class Solution:
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)

        for i in range(int(math.log(n, 2)), 1, -1):
            k = int(n ** i ** -1)
            if (k ** (i + 1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)


if __name__ == '__main__':
    print(Solution().smallestGoodBase('13'))
