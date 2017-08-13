class Solution(object):
    def generateParenthesis(self, n):
        result = []
        nSets = []
        nLt = []
        for i in range(n, 0, -1):
            nLt.append(2 * n - i)

        nSets = self.jumpNumber(nLt, 0)
        print(nSets)
        result = list(map(self.genParenthesisByNumbers, nSets))
        return result

    def jumpNumber(self, nLt, digit):
        result = []
        result.append(tuple(nLt))
        while digit < len(nLt) and nLt[digit] > digit * 2 + 1:
            nLt[digit] -= 1
            if digit > 0 and nLt[digit] <= nLt[digit - 1]:
                break
            result.extend(self.jumpNumber(nLt[:], digit + 1))
        return result

    def genParenthesisByNumbers(self, nLt):
        result = ''
        for i in range(nLt[-1] + 1):
            if i in nLt:
                result += ')'
            else:
                result += '('
        return result


if __name__ == '__main__':
    # print(Solution().jumpNumber([3, 4, 5], 0))
    # print(Solution().jumpNumber([2, 4, 5], 0))
    # print(Solution().generateParenthesis(1))
    # print(Solution().generateParenthesis(2))
    # print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))
