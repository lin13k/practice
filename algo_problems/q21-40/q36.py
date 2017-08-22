from collections import Counter

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            line = board[i]
            cd = Counter(line)
            for items in cd.items():
                if items[1] > 1 and items[0] != '.':
                    return False

            line = [board[j][i] for j in range(9)]
            cd = Counter(line)
            for items in cd.items():
                if items[1] > 1 and items[0] != '.':
                    return False

            line = [board[j % 3 + (i % 3) * 3][j // 3 + (i // 3) * 3] for j in range(9)]
            cd = Counter(line)
            for items in cd.items():
                if items[1] > 1 and items[0] != '.':
                    return False
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