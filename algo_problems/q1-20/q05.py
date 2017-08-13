class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        bloatedS = self.injectDummyChar(s)
        paliCounts = [0 for i in range(len(bloatedS))]
        anchor = 0
        right = 0
        max_index = 0
        for i in range(1, len(bloatedS)):
            mirror = anchor * 2 - i
            if i + paliCounts[mirror] < right:
                paliCounts[i] = min(paliCounts[mirror], len(bloatedS) - i)
            else:
                # paliCounts[i] = paliCounts[mirror]
                plen = self.findPalindromeLengthAtGivenIndex(
                    bloatedS, i, paliCounts[i])
                paliCounts[i] += plen
                right = i + plen
                if plen > 0:
                    anchor = i
                    right = i + plen
                    if plen > paliCounts[max_index]:
                        max_index = i
        print(paliCounts, max_index, bloatedS)
        # print(max_index//2, paliCounts[max_index]//2, (paliCounts[max_index]+1)//2)
        return s[(max_index - paliCounts[max_index])//2:(max_index + paliCounts[max_index]+1)//2]
        # return bloatedS[max_index - paliCounts[max_index]:
        #                 max_index + paliCounts[max_index] + 1].replace('#', '')

    def findPalindromeLengthAtGivenIndex(self, s, index, bias):
        tmpLen = 0
        if index >= len(s) or index < 0:
            raise Exception('value error')

        for i, c in enumerate(s[index + 1 + bias:]):
            if s[index - i - 1] == c:
                tmpLen += 1
            else:
                break
        return tmpLen

    def injectDummyChar(self, s):
        tmpLt = []
        for i in range(len(s)):
            tmpLt.append('#' + s[i])
        tmpLt.append('#')
        return ''.join(tmpLt)

        # return '#'+("#".join(list(s)))+'#'

if __name__ == '__main__':
    # assert(Solution().longestPalindrome("abb") == 'bb')
    # assert(Solution().longestPalindrome("abba") == 'abba')
    # assert(Solution().longestPalindrome("abcb") == 'bcb')
    print(Solution().longestPalindrome("ressed"))
    print(Solution().longestPalindrome("ressedessed"))
    print(Solution().longestPalindrome("babadada"))
    # assert(Solution().longestPalindrome("stressed") == 'esse')
    
