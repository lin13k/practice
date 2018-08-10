class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        d = {}
        for pair in pairs:
            w1, w2 = pair
            if w1 not in d and w2 not in d:
                d[w1] = d[w2] = {w1, w2}
            elif w1 not in d:
                d[w2].add(w1)
                d[w1] = d[w2]
            elif w2 not in d:
                d[w1].add(w2)
                d[w2] = d[w1]
            elif d[w1] is not d[w2]:
                for w in d[w1]:
                    d[w2].add(w)
                    d[w] = d[w2]

        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            if w1 != w2 and ((w1 not in d or w2 not in d)or d[w1] is not d[w2]):
                return False
        return True


if __name__ == '__main__':
    print(Solution().areSentencesSimilarTwo(['a', 'b', 'C'], [
          'A', 'B', 'c'], [['a', 'A'], ['B', 'b'], ['c', 'C']]))
    print(Solution().areSentencesSimilarTwo(
        ["yesterday", "james", "have", "an", "extraordinary", "meal"],
        ["yesterday", "james", "take", "one", "good", "dinner"],
        [
            ["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"], ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"], ["vehicle", "car"], [
                "entertain", "have"], ["drink", "have"], ["eat", "have"], ["take", "have"], ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"], ["actually", "very"], ["really", "very"], ["super", "very"]]
    ))
