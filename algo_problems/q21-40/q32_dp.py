class Solution(object):
    def longestValidParentheses(self, s):
        dpLt = [0 for i in s]
        for i in range(1, len(s)):
            if s[i] == ')' and s[i - 1] == '(':
                dpLt[i] = 2 if i < 2 else dpLt[i - 2] + 2
            elif s[i] == ')' and s[i - 1] == ')':
                tmpIndex = i - dpLt[i - 1] - 1
                if tmpIndex >= 0 and s[tmpIndex] == '(':
                    dpLt[i] = dpLt[i - 1] + dpLt[tmpIndex - 1] + 2
        return 0 if len(dpLt) == 0 else max(dpLt)


if __name__ == '__main__':
    # print(Solution().longestValidParentheses(''))
    # print(Solution().longestValidParentheses('())'))
    print(Solution().longestValidParentheses("(()))())("))
    # print(Solution().longestValidParentheses('(()'))
    # print(Solution().longestValidParentheses('))(()'))
    # print(Solution().longestValidParentheses(')))(('))
    # print(Solution().longestValidParentheses('(())()('))

    # print(Solution().longestValidParentheses(")()(((())))("))
    # print(Solution().longestValidParentheses("))()(((())))(("))
