class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n <= 1:
            return True

        if A[0] > A[-1]:
            # decreasing check
            for i in range(1, n):
                if A[i - 1] < A[i]:
                    return False
        else:
            for i in range(1, n):
                if A[i - 1] > A[i]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().isMonotonic([1, 2, 2, 2, 3, 4, 5, 6, 7]))
    print(Solution().isMonotonic([1, 2, 2, 2, 3, 4, 5, 6, 7, 6]))
    print(Solution().isMonotonic([6, 6, 5, 5, 4, 3, 2, 1]))
    print(Solution().isMonotonic([6, 6, 5, 5, 6, 3, 2, 1]))
