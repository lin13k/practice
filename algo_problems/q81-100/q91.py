class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        dpTable = [1]
        if s[-1] == '0':
            dpTable.append(0)
            if s[-2] not in ['1', '2']:
                return 0
        else:
            dpTable.append(1)

        for i in range(len(s) - 1):
            if s[i:i + 2] == '00':
                return 0
            elif s[i] == '0':
                if s[i - 1] in ['1', '2']:
                    dpTable[-1] -= 1
                else:
                    return 0
            elif int(s[i:i + 2]) <= 26:
                dpTable.append(dpTable[-1] + dpTable[-2])
            else:
                dpTable.append(dpTable[-1])
        print(dpTable)
        return dpTable[-1]


if __name__ == '__main__':
    # print(Solution().numDecodings('1'))
    # print(Solution().numDecodings('12'))
    # print(Solution().numDecodings('123'))
    # print(Solution().numDecodings('3'))
    # print(Solution().numDecodings('32'))
    # print(Solution().numDecodings('321'))
    # print(Solution().numDecodings('00'))
    # print(Solution().numDecodings('01'))
    # print(Solution().numDecodings('26'))
    # print(Solution().numDecodings('1'))
    # print(Solution().numDecodings('10'))
    # print(Solution().numDecodings('100'))
    # print(Solution().numDecodings('101'))
    # print(Solution().numDecodings('01'))
    # print(Solution().numDecodings('230'))
    print(Solution().numDecodings('1010'))
    # print(Solution().numDecodings('1111'))

    # 1 1 1 1
    # 11 1 1
    # 1 11 1
    # 1 1 11
    # 11 11
    #
    # 1 1 1 1 1
    # 11 1 1 1
    # 1 11 1 1
    # 1 1 11 1
    # 1 1 1 11
    # 11 11 1
    # 11 1 11
    # 1 11 11
