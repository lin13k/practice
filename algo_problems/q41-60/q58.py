class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0
        tmpLt = s.split()
        return len(tmpLt[-1]) if len(tmpLt) != 0 else 0

if __name__ == '__main__':
    print(Solution().lengthOfLastWord('a '))
    print(Solution().lengthOfLastWord("b   a    "))