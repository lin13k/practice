class Solution(object):
    def generateParenthesis(self, n):
        def generator(s, openN, closeN):
            if openN > 0:
                for q in generator(s + '(', openN - 1, closeN):
                    yield q
            if openN < closeN:
                for q in generator(s + ')', openN, closeN - 1):
                    yield q
            if closeN == 0:
                yield s
        return list(generator('', n, n))


if __name__ == '__main__':
    # print(Solution().jumpNumber([3, 4, 5], 0))
    # print(Solution().jumpNumber([2, 4, 5], 0))
    # print(Solution().generateParenthesis(1))
    # print(Solution().generateParenthesis(2))
    # print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))
