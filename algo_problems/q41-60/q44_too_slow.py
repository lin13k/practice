class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match(s, p)

    def match(self, s, p):
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        if len(s) == 0:
            if p[0] != '*':
                return False

        if p[0] != '*':
            if s[0] == p[0] or p[0] == '?':
                return self.match(s[1:], p[1:])

            else:
                return False

        else:
            result = False
            for i in range(len(s) + 1):
                result = result or self.match(s[i:], p[1:])
                if result:
                    return True
            return result
