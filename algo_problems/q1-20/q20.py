class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openMark = '([{'
        markMatch = {'(': ')', '[': ']', '{': '}'}
        tmpLt = []
        for i in s:
            if i in openMark:
                tmpLt.append(i)
            else:
                if tmpLt == []:
                    return False
                else:
                    if markMatch[tmpLt[-1]] != i:
                        return False
                    else:
                        tmpLt.pop()
        if tmpLt != []:
            return False

        return True
