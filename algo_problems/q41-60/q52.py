class Solution(object):
    def totalNQueens(self, n):
        candidates = [i for i in range(1, n + 1)]
        return self.search(candidates, [])

    def search(self, candidates, path):
        if len(candidates) == 0:
            return 1
        else:
            result = 0
            for i in range(len(candidates)):
                if self.check(candidates[i], path):
                    result += self.search(
                        candidates[:i] + candidates[i + 1:], path + [candidates[i]])
            return result

    def check(self, n, path):
        for i in range(1, len(path) + 1):
            if n + i == path[-i] or n - i == path[-i]:
                return False
        return True


if __name__ == '__main__':
    # print(Solution().check(2, [4, 1, 3]))
    # print(Solution().check(3, [2, 4, 1]))
    print(Solution().solveNQueens(4))
