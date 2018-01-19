class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def getSurroundLiveCount(i, j):
            posI = (i - 1, i - 1, i - 1, i, i + 1, i + 1, i + 1, i)
            posJ = (j - 1, j, j + 1, j + 1, j + 1, j, j - 1, j - 1)
            return sum(list(map(lambda x, y: board[x][y], posI, posJ)))

        liveMask = 1
        nextMask = 1 << 1

        for i in range(len(board)):
            for j in range(len(board[i])):
                cnt = getSurroundLiveCount(i, j)
                if board[i][j] == 1:
                    if cnt == 2:
                        board[i][j] = board[i][j] | nextMask
                else:
                    if cnt == 3:
                        board[i][j] = board[i][j] | nextMask

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] >>= 1


if __name__ == '__main__':
    print(Solution().getSurroundLiveCount(1, 1, [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0]]))
    print(Solution().getSurroundLiveCount(0, 1, [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0]]))
