class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hashDict = {'': 1}
        for word in wordDict:
            hashDict[word] = 1
        # print(hashDict)

        queue = [s]

        while len(queue) != 0:
            tmp = queue.pop(0)
            if tmp in hashDict:
                return True
            for i in range(len(tmp)-1, 0, -1):
                if tmp[:i] in hashDict:
                    queue.append(tmp[i:])
            # print(queue)
        return False

if __name__ == '__main__':
    print(Solution().wordBreak('abcd',['a','bc','d']))