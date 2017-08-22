class Solution(object):
    def isValidSudoku(self, board):
        rowCheck = [[False for i in range(9)] for j in range(9)]
        columnCheck = [[False for i in range(9)] for j in range(9)]
        squareCheck = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    checkNum = int(board[i][j]) - 1
                    k = (i // 3) * 3 + j // 3
                    if rowCheck[i][checkNum] or columnCheck[j][checkNum] or squareCheck[k][checkNum]:
                        return False
                    rowCheck[i][checkNum], columnCheck[j][checkNum], squareCheck[k][checkNum] = True, True, True
        return True


if __name__ == '__main__':
    # b = [
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9'],
    #     ['1','2','3','4','5','6','7','8','9']
    # ]

    # print(Solution().isValidSudoku(b))

    b = [
        ".9..4....",
        "1.....6..",
        "..3......",
        ".........",
        "...7.....",
        "3...5....",
        "..7..4...",
        ".........",
        "....7...."]
    print(Solution().isValidSudoku(b))