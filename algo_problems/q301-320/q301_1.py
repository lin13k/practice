class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def remove(s, lastSearched, lastRemoved, p):
            cnt = 0
            for i in range(lastSearched, len(s)):
                if s[i] == p[0]:
                    cnt += 1
                elif s[i] == p[1]:
                    cnt -= 1
                if cnt < 0:
                    for j in range(lastRemoved, i + 1):
                        if s[j] == p[1] and\
                                (j == lastRemoved or s[j] != s[j - 1]):
                            remove(s[:j] + s[j + 1:], i, j, p)
                    return
            if p[0] == '(':
                remove(s[::-1], 0, 0, [')', '('])
            else:
                result.append(s[::-1])
        remove(s, 0, 0, ['(', ')'])
        return result


if __name__ == '__main__':
    print(Solution().removeInvalidParentheses('()())()'))
