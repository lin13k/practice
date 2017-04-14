class Solution(object):
    def longestPalindrome(self, s):
        bs = '#' + ('#'.join(list(s))) + '#'
        p = [0 for i in range(len(bs))]
        anchor = 0
        right = 0
        max_int = 0
        max_index = 0
        for i in range(1, len(p)):

            # print('['+'-----'*i + ('--%s--' % i ) + '-----'*(len(bs) -i))
            # print(list(map(str,p)), i)
            # print(list(bs))
            mirror = max(anchor * 2 - i, 0)
            if i + p[mirror] < right:
                p[i] = p[mirror]
            else:
                if i < right:
                    p[i] = (right - i) + self.findPalindromeLengthAtGivenIndex(bs, i, (right - i))
                else:
                    p[i] = self.findPalindromeLengthAtGivenIndex(bs, i, 0)
                
                if p[i] + i > right:
                    right = i + p[i]
                    anchor = i
                    if p[i] > max_int:
                        max_int = p[i]
                        max_index = i
        # print(s, (max_index - p[max_index]) // 2, (max_index + p[max_index] + 1) // 2)
        # print(p, max_index, bs)
        return s[(max_index - p[max_index]) // 2:(max_index + p[max_index] + 1) // 2]

    def findPalindromeLengthAtGivenIndex(self, s, index, bias):
        # print(s,index,bias)
        tmpLen = 0
        if index >= len(s) or index < 0:
            raise Exception('value error')

        for i, c in enumerate(s[index + 1 + bias:]):
            if index - i - 1 < 0:
                break
            if s[index - i - 1 - bias] == c:
                tmpLen += 1
            else:
                break
        # print(tmpLen)
        return tmpLen

if __name__ == '__main__':
    assert(Solution().longestPalindrome("abb") == 'bb')
    assert(Solution().longestPalindrome("abba") == 'abba')
    assert(Solution().longestPalindrome("abcb") == 'bcb')

# #     print(Solution().findPalindromeLengthAtGivenIndex('#c#c#c#', 3, 1))
# #     print(Solution().longestPalindrome("ccc"))
# #     print(Solution().longestPalindrome("ressedessed"))
    print(Solution().longestPalindrome("babadada"))
    print(Solution().longestPalindrome("a"))
    
    # assert(Solution().longestPalindrome("stressed") == 'esse')
