from functools import reduce


class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            strs.append('')

        def findCommon(s1, s2):
            if len(s1) > len(s2):
                s2, s1 = s1, s2
            tmpIndex = -1
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    break
                tmpIndex = i
            return s1[:tmpIndex + 1]

        result = reduce(findCommon, strs)
        return result


if __name__ == '__main__':

    print(Solution().longestCommonPrefix([
        'abc',
        'abcd',
        'abcde'
    ]))

    print(Solution().longestCommonPrefix([
        ""
    ]))

    print(Solution().longestCommonPrefix([

    ]))

    print(Solution().longestCommonPrefix([
        'a',
        'b'
    ]))

    print(Solution().longestCommonPrefix([
        'ab',
        'a'
    ]))
