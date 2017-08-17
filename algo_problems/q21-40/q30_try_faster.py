from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        if len(s) == 0 and words == ['']:
            return [0]
        wordLength = len(words[0])
        wordN = len(words)
        if len(s) < wordN * wordLength:
            return []
        wordsDict = self.count(words)
        result = []
        winSize = wordLength * (wordN - 1)
        for i in range(wordLength):
            countDict = {}
            for j in range(wordN - 1):
                tmp = i + j * wordLength
                word = s[tmp: tmp + wordLength]
                self.addCount(countDict, word)
            index = i + winSize
            while index < len(s) - wordLength + 1:
                word = s[index: index + wordLength]
                self.addCount(countDict, word)
                if countDict == wordsDict:
                    result.append(index - winSize)
                removeWord = s[index - winSize:
                               index - winSize + wordLength]
                self.minusCount(countDict, removeWord)
                index += wordLength
        return result
    def count(self, words):
        return Counter(words)
    def addCount(self, d, word):
        if word in d: d[word] += 1
        else: d[word] = 1
    def minusCount(self, d, word):
        d[word] -= 1
        if d[word] == 0: del(d[word])

if __name__ == '__main__':
    assert(Solution().findSubstring('abcdefhgkdefabc', ['abc', 'def'])==[0,9])
    assert(Solution().findSubstring(
        'barfoofoobarthefoobarman', ["bar", "foo", "the"])==[6,9,12])
    assert(Solution().findSubstring(
        'wordgoodgoodgoodbestword', ["word","good","best","good"])==[8])
    assert(Solution().findSubstring(
        'lingmindraboofooowingdingbarrwingmonkeypoundcake',
        ["fooo", "barr", "wing", "ding", "wing"]) == [13])
