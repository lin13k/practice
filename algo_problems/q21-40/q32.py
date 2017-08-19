class Solution(object):
    def longestValidParentheses(self, s):

        left = 0
        right = 0
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                result = max(result, left + right)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                result = max(result, left + right)
            elif right < left:
                left = 0
                right = 0
        return result


if __name__ == '__main__':
    print(Solution().longestValidParentheses('())'))
    print(Solution().longestValidParentheses('(()'))
    print(Solution().longestValidParentheses('))(()'))
    print(Solution().longestValidParentheses(')))(('))
    print(Solution().longestValidParentheses('(())()('))

    print(Solution().longestValidParentheses(")()(((())))("))
    print(Solution().longestValidParentheses("))()(((())))(("))
