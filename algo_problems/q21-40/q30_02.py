class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import collections
        wd = collections.Counter(words)
        wn = len(words)
        wl = len(words[0])
        tl = wn * wl
        result = []
        for i in range(wl):
            tmpDict = wd.copy()
            wc = 0
            for j in range(i, len(s) - wl + 1, wl):
                tmpStr = s[j:j + wl]
                # print('tmpStr', tmpStr)
                if tmpStr not in tmpDict:
                    tmpDict = wd.copy()
                    wc = 0
                    continue
                tmpDict[tmpStr] -= 1
                if tmpDict[tmpStr] >= 0:
                    wc += 1
                else:
                    while tmpDict[tmpStr] < 0:
                        ds = s[j - wc * wl:j - wc * wl + wl]
                        # print('ds', ds)
                        tmpDict[ds] += 1
                        if tmpDict[ds] < 0:
                            wc += 1
                        elif tmpDict[ds] > 0:
                            wc -= 1
                # print(wc)
                if wc == wn:
                    result.append(j - tl + wl)
        return result


if __name__ == '__main__':
    print(Solution().findSubstring('abcdefhgkdefabc', ['abc', 'def']))
    # print(Solution().findSubstring(
    #     'aabbbbaacc', ["aa", "bb", "cc"]))
    print(Solution().findSubstring(
        'barfoofoobarthefoobarman', ["bar", "foo", "the"]))
    # assert(Solution().findSubstring(
    #     'barfoofoobarthefoobarman', ["bar", "foo", "the"])==[6,9,12])
    # assert(Solution().findSubstring(
    #     'wordgoodgoodgoodbestword', ["word","good","best", "good"])==[12])
    # print(Solution().findSubstring('abbbca',['a','b','c','b']))
    # print(Solution().findSubstring('abcdc',['a','b','c','d','c']))
    # assert(Solution().findSubstring(
    #     'lingmindraboofooowingdingbarrwingmonkeypoundcake',
    #     ["fooo", "barr", "wing", "ding", "wing"]) == [13])
    #
    print(Solution().findSubstring(
        "abbaccaaabcabbbccbabbccabbacabc"
        "acbbaabbbbbaaabaccaacbccabcbaba"
        "bbbabccabacbbcabbaacaccccbaabca"
        "baabaaaabcaabcacabaa", ["cac", "aaa", "aba", "aab", "abc"]))
