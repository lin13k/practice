class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        candidates = [i for i in range(1, n + 1)]
        result = []
        self.search(candidates, [], result)
        return self.render(result)

    def render(self, data):
        result = []
        if len(data) == 0:
            return result
        if len(data[0]) == 0:
            return result

        length = len(data[0])
        for i in range(len(data)):
            tmp = []
            for j in range(length):
                tmp.append('.' * (data[i][j] - 1) +
                           'Q' + '.' * (length - data[i][j]))
            result.append(tmp)
        return result

    def search(self, candidates, path, rec):
        if len(candidates) == 0:
            rec.append(path)
        else:
            for i in range(len(candidates)):
                if self.check(candidates[i], path):
                    self.search(
                        candidates[:i] + candidates[i + 1:], path + [candidates[i]], rec)

    def check(self, n, path):
        for i in range(1, len(path) + 1):
            if n + i == path[-i] or n - i == path[-i]:
                return False
        return True


if __name__ == '__main__':
    # print(Solution().check(2, [4, 1, 3]))
    # print(Solution().check(3, [2, 4, 1]))
    print(Solution().solveNQueens(4))
