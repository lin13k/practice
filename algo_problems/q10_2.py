class Solution(object):
    memoryCache = {}

    def isMatch(self, s, p):
        p = self.shiftPattern(p)
        return self.recursiveSearch(s, p)

    def recursiveSearch(self, s, p):
        if (s, p) in self.memoryCache:
            return self.memoryCache[(s, p)]
        if len(s) == 0:
            if len(p) == 0:
                return True
            else:
                if len(p) == 2 and p[1] == '*':
                    return True
        if len(p) == 0:
            return False

        result = False
        if len(s) > 0:
            if self.matchChar(s[0], p[0]):
                if self.is_decorated(p):
                    self.memoryCache[(s, p[2:])] = self.recursiveSearch(s, p[2:])
                    result = result or self.memoryCache[(s, p[2:])]
                    s = s[1:]
                else:
                    s = s[1:]
                    p = p[1:]
            else:
                if self.is_decorated(p):
                    p = p[2:]
                else:
                    return False
            self.memoryCache[(s, p)] = self.recursiveSearch(s, p)
            result = result or self.memoryCache[(s, p)]
        else:
            if self.is_decorated(p):
                p = p[2:]
            else:
                return False
            self.memoryCache[(s, p)] = self.recursiveSearch(s, p)
            result = result or self.memoryCache[(s, p)]

        return result

    def matchChar(self, c, pc):
        if c == pc or pc == '.':
            return True
        return False

    def is_decorated(self, p):
        if len(p) < 2:
            return False
        if p[1] != '*':
            return False
        return True

    def shiftPattern(self, p):
        result = p
        asteriskPosition = [pos for pos, char in enumerate(p) if char == '*']
        for i in asteriskPosition:
            if i == 0:
                raise Exception('no preceding element')
            precedingChar = p[i - 1]
            lastPos = 0
            rightStr = p[i + 1:]
            for j in range(len(rightStr)):
                if rightStr[j] == precedingChar:
                    lastPos += 1
                else:
                    if rightStr[j] == '*':
                        lastPos -= 1
                    break
            if lastPos != 0:
                result = p[:i] + p[i + lastPos] + \
                    p[i + 1:i + lastPos] + p[i] + p[i + lastPos + 1:]

        return result


if __name__ == '__main__':
    assert(Solution().isMatch("aa", "a") == False)
    assert(Solution().isMatch("aa", "aa") == True)
    assert(Solution().isMatch("aaa", "aa") == False)
    assert(Solution().isMatch("aa", "a*") == True)
    assert(Solution().isMatch("aa", ".*") == True)
    assert(Solution().isMatch("ab", ".*") == True)
    assert(Solution().isMatch("aab", "c*a*b") == True)
    assert(Solution().isMatch("ab", ".*c") == False)
    assert(Solution().isMatch("aaa", "a.a") == True)
    assert(Solution().isMatch("aaa", "ab*a") == False)
    assert(Solution().isMatch("a", "ab*") == True)
    assert(Solution().isMatch("aaba", "ab*a*c*a") == False)
    assert(Solution().isMatch("aaa", "ab*a*c*a") == True)
    assert(Solution().isMatch("aaa", "a*a") == True)
    assert(Solution().isMatch("ab", ".*..c*") == True)
    assert(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False)