class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        readDigit = False
        digit = ''
        stack = []
        currentString = ''
        for c in s:
            if c >= '0' and c <= '9':
                if not readDigit:
                    stack.append(currentString)
                    currentString = ''
                readDigit = True
                digit += c
            elif c == '[':
                readDigit = False
                stack.append(int(digit))
                digit = ''
            elif c == ']':
                currentString *= stack.pop()
                currentString = stack.pop() + currentString
            else:
                currentString += c
        return currentString


if __name__ == '__main__':
    assert(Solution().decodeString('abc3[a]') == 'abcaaa')
    assert(Solution().decodeString('3[2[a]]') == 'aaaaaa')
    assert(Solution().decodeString('3[d2[a]]') == 'daadaadaa')
