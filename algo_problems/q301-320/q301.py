class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for i in range(len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        level = {s}
        while True:
            result = filter(isValid, level)
            if result:
                return result
            tmpLevel = set()
            for x in level:
                for i in range(len(x)):
                    tmpLevel.add(x[:i] + x[i + 1:])
            level = tmpLevel


if __name__ == '__main__':
    print(Solution().removeInvalidParentheses('()())()'))
