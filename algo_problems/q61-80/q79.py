class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0:
            if len(word) == 0:
                return True
            else:
                return False

        result = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                result = self.check_exist(board, word, i, j, 0)
                if result:
                    return True
        return result

    def check_exist(self, board, word, i, j, k):
        if k == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False

        if board[i][j][-1] == '*' or board[i][j][0] != word[k]:
            return False

        # mark it
        board[i][j] = board[i][j] + '*'

        result = (self.check_exist(board, word, i + 1, j, k + 1) or
                  self.check_exist(board, word, i - 1, j, k + 1) or
                  self.check_exist(board, word, i, j + 1, k + 1) or
                  self.check_exist(board, word, i, j - 1, k + 1))

        # unmark it
        board[i][j] = board[i][j][:1]

        return result


if __name__ == '__main__':
    print(Solution().exist([
        ['a', 'b', 'c'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c']
    ], 'bccb'))

    print(Solution().exist([
        ['a', 'b', 'c'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c']
    ], 'bcb'))
