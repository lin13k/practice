class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        startPoint = n * n

        matrix = [[startPoint]]

        i = startPoint - 1
        while i > 0:
            edgeLen = len(matrix[0])
            matrix.append([j for j in range(i, i - edgeLen, -1)])
            i -= edgeLen
            matrix = list(zip(*matrix[::-1]))

        return list(zip(*matrix[::-1]))


if __name__ == '__main__':
    print(Solution().generateMatrix(1))
    print(Solution().generateMatrix(2))
    print(Solution().generateMatrix(3))
