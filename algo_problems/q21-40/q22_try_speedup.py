class Solution(object):
    def generateParenthesis(self, n):
        def generate(s, openN, closeN, result):
            if openN > 0:
                generate(s + '(', openN - 1, closeN, result)
            if openN < closeN:
                generate(s + ')', openN, closeN - 1, result)
            if closeN == 0:
                result.append(s)
        result = []
        generate('', n, n, result)
        return result
if __name__ == '__main__':
    # print(Solution().jumpNumber([3, 4, 5], 0))
    # print(Solution().jumpNumber([2, 4, 5], 0))
    # print(Solution().generateParenthesis(1))
    # print(Solution().generateParenthesis(2))
    # print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))
