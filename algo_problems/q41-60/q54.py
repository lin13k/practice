class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        offsetList = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        offset = offsetList[0]
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        result = []
        i = 0
        offsetIdx = 0
        pos = [0, 0]
        turnCount = 1
        while i < m * n:
            print(pos)
            result.append(matrix[pos[0]][pos[1]])
            pos[0] += offset[0]
            pos[1] += offset[1]
            if offset[0] != 0:
                if pos[0] < 0 + (turnCount//4) or pos[0] == m - (turnCount//4):
                    pos[0] = 0 + (turnCount//4) if pos[0] < 0 + (turnCount//4) else m - 1 - (turnCount//4)
                    offsetIdx = (offsetIdx + 1) % 4
                    offset = offsetList[offsetIdx]
                    pos[1] += offset[1]
                    turnCount += 1
            if offset[1] != 0:
                if pos[1] < 0 + (turnCount//4) or pos[1] == n - (turnCount//4):
                    pos[1] = 0 + (turnCount//4) if pos[1] < 0 + (turnCount//4) else n - 1 - (turnCount//4)
                    offsetIdx = (offsetIdx + 1) % 4
                    offset = offsetList[offsetIdx]
                    pos[0] += offset[0]
                    turnCount += 1
            i += 1
        return result


if __name__ == '__main__':
    a = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45]
    ]
    # a = [
    #     [11,12,13],
    #     [21,22,23],
    #     [31,32,33],
    #     [41,42,43]
    # ]
    print(Solution().spiralOrder(a))
