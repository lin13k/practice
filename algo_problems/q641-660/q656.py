class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if A[-1] == -1:
            return []
        if len(A) != 1 and B == 0:
            return []

        n = len(A)
        pathTable = {n - 1: [n]}
        sumTable = {n - 1: A[n - 1]}
        for i in range(n - 2, -1, -1):
            if A[i] == -1:
                continue
            for j in range(i + 1, n if i + B + 1 >= n else i + B + 1):
                if j not in sumTable:
                    continue
                if i not in sumTable or sumTable[i] > A[i] + sumTable[j]:
                    sumTable[i] = A[i] + sumTable[j]
                    pathTable[i] = [i + 1] + pathTable[j]

        return pathTable[0] if 0 in pathTable else []


if __name__ == '__main__':
    print(Solution().cheapestJump([1, 2, 4, -1, 2], 2))
    print(Solution().cheapestJump([1, 2, 4, -1, 2], 1))
