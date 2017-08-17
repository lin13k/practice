from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):

        if len(words) == 0:
            return []
        if len(s) == 0 and words == ['']:
            return [0]

        result = []
        wordLength = len(words[0])
        for i in range(wordLength):
            tmpLt = [j + i for j in self.check(s[i:], words, wordLength)]
            result.extend(tmpLt)
        result.sort()
        return result

    def check(self, s, words, wordLength):
        i = 0
        result = []

        tmpWords = self.count(words)
        headIndex = i

        while i < len(s) - wordLength + 1:
            if s[i:i + wordLength] in tmpWords:
                tmpWords[s[i:i + wordLength]] -= 1
                if tmpWords[s[i:i + wordLength]] == 0:
                    del(tmpWords[s[i:i + wordLength]])
                if len(tmpWords) == 0:
                    result.append(headIndex)
                    tmpWords = self.count(words)
                    headIndex = headIndex + wordLength
                    i = headIndex
                    continue

            else:
                tmpWords = self.count(words)
                i = headIndex
                headIndex = headIndex + wordLength

            i += wordLength
        return result

    def count(self, words):
        return Counter(words)


if __name__ == '__main__':
    # assert(Solution().findSubstring('abcdefhgkdefabc', ['abc', 'def'])==[0,9])
    # assert(Solution().findSubstring(
    #     'barfoofoobarthefoobarman', ["bar", "foo", "the"])==[6,9,12])
    # assert(Solution().findSubstring(
    #     'wordgoodgoodgoodbestword', ["word","good","best","good"])==[8])

    assert(Solution().findSubstring(
        'lingmindraboofooowingdingbarrwingmonkeypoundcake',
        ["fooo", "barr", "wing", "ding", "wing"]) == [13])
