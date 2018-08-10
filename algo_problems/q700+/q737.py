class DisjointSetUnion:
    def __init__(self, N):
        self.par = [i for i in range(N)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)


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
        sset = set()
        for pair in pairs:
            sset.add(pair[0])
            sset.add(pair[1])
        words = list(sset)
        indexes = {words[i]: i for i in range(len(words))}
        dsu = DisjointSetUnion(len(indexes))
        for pair in pairs:
            dsu.union(indexes[pair[0]], indexes[pair[1]])

        tokens1 = []
        for word in words1:
            try:
                tokens1.append(dsu.find(indexes[word]))
            except Exception as e:
                tokens1.append(word)
        tokens2 = []
        for word in words2:
            try:
                tokens2.append(dsu.find(indexes[word]))
            except Exception as e:
                tokens2.append(word)
        return all(tokens1[i] == tokens2[i] for i in range(len(words1)))


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
