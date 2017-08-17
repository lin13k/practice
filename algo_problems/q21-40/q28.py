class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            j = 0

            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                else:
                    if j == len(needle) - 1:
                        return i
                j += 1
        return -1
