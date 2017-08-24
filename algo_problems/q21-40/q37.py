class Solution(object):
    def preprocess(self, board):
        result = []
        for i in range(9):
            tmpLt = []
            for j in range(9):
                tmpLt.append(board[i][j])
            result.append(tmpLt)
        return result


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # check first
        # board = self.preprocess(board)
        rowCheck = [[False for i in range(9)] for j in range(9)]
        columnCheck = [[False for i in range(9)] for j in range(9)]
        squareCheck = [[False for i in range(9)] for j in range(9)]
        countDict = {i:0 for i in range(9)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    checkNum = int(board[i][j]) - 1
                    k = (i // 3) * 3 + j // 3
                    if rowCheck[i][checkNum] or columnCheck[j][checkNum] or squareCheck[k][checkNum]:
                        return False
                    rowCheck[i][checkNum], columnCheck[j][checkNum], squareCheck[k][checkNum] = True, True, True
                    if checkNum in countDict:
                        countDict[checkNum] += 1

        priorityLt = [i[0] for i in sorted(list(countDict.items()),
            key=lambda x: x[1])[::-1]]

        self.search(board, 0, rowCheck, columnCheck, squareCheck, priorityLt)

    def search(self, board, pos, rc, cc, sc, pr):

        if pos >= 81:
            return True

        i = pos // 9
        j = pos % 9
        if board[i][j] != '.':
            return self.search(board, pos + 1, rc, cc, sc, pr)
        k = (i // 3) * 3 + j // 3
        for candidate in pr:
            if rc[i][candidate] or cc[j][candidate] or sc[k][candidate]:
                continue
            else:
                rc[i][candidate], cc[j][candidate], sc[k][candidate] = True, True, True
                
                # board[i][j] = str(candidate + 1) // code for leetcode
                board[i] = board[i][:j] + str(candidate + 1) + board[i][j+1:]
                
                if self.search(board, pos + 1, rc, cc, sc, pr):
                    return True
                else:
                    rc[i][candidate], cc[j][candidate], sc[k][candidate] = False, False, False
                    
                    # board[i][j] = '.' // code for leetcode
                    board[i] = board[i][:j] + '.' + board[i][j+1:]

        return False


if __name__ == '__main__':
    data = [".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
    Solution().solveSudoku(data)
    print(data)

    data = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    Solution().solveSudoku(data)
    print(data)