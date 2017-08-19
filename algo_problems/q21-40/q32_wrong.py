class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmpCount = 0
        markFlag = False
        head = 0
        result = 0
        for i in range(len(s)):
            tmpCount += 1 if s[i] == '(' else -1
            if tmpCount > 0:
                # start marking
                if not markFlag:
                    markFlag = True
                    head = i
            elif tmpCount < 0:
                if markFlag:
                    result = max(result,  i - head)
                markFlag = False
                tmpCount = 0
        if markFlag:
            result = max(result, i - head +1 - tmpCount)
        markFlag = False
        tmpCount = 0
        head = 0
        for i in range(len(s)-1, -1, -1):
            tmpCount += 1 if s[i] == ')' else -1
            if tmpCount > 0:
                # start marking
                if not markFlag:
                    markFlag = True
                    head = i
            elif tmpCount < 0:
                if markFlag:
                    result = max(result, head - i)
                markFlag = False
                tmpCount = 0
        if markFlag:
            result = max(result, head - i + 1 - tmpCount)

        return result


if __name__ == '__main__':
    # print(Solution().longestValidParentheses('())'))
    # print(Solution().longestValidParentheses('(()'))
    # print(Solution().longestValidParentheses('))(()'))
    # print(Solution().longestValidParentheses(')))(('))
    # print(Solution().longestValidParentheses('(())()('))

    print(Solution().longestValidParentheses(")()(((())))("))
    print(Solution().longestValidParentheses("))()(((())))(("))