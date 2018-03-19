from collections import defaultdict
import sys

# 11 including protocols and subdomains, 5 is the minimum from mail
PARTIAL_MATCH_THRESHOLD = 11 + 5


class TrieTreeNode:

    def __init__(self):
        self.children = defaultdict(TrieTreeNode)
        self.exist = False


class TrieTree:

    def __init__(self):
        self.root = TrieTreeNode()

    def build(self, records):
        for record in records:
            self.insert(record)

    def insert(self, record):
        currentNode = self.root
        for c in record:
            currentNode = currentNode.children[c]
        currentNode.exist = True

    '''
    search(query)
    input: string of query
    output: int of result
        1 match
        0 partial match
        -1 not match
    '''

    def search(self, query):
        currentNode = self.root
        matchCount = 0
        for c in query:
            currentNode = currentNode.children.get(c)
            if currentNode is None:
                return -1 if matchCount < PARTIAL_MATCH_THRESHOLD else 0
            matchCount += 1
        return 1


class Solution:

    def matchQuery(self, file=None):
        backload_urls, queries = self._getInput(file)
        result = []
        trieTree = TrieTree()
        trieTree.build(backload_urls)

        for query in queries:
            result.append(trieTree.search(query))

        self._outputResult(result)

    def _outputResult(self, results):
        for result in results:
            if result == 1:
                print('FULL URL FOUND')
            elif result == -1:
                print('NO URL FOUND')
            else:
                print('PARTIAL URL FOUND')

    def _getInput(self, file=None):
        if file is not None:
            backload_urls = file.readline().rstrip().split(',')
            lineCount = int(file.readline())
            queries = []
            while lineCount > 0:
                queries.append(file.readline().rstrip())
                lineCount -= 1
        else:
            backload_urls = input('backload_urls:').split(',')
            lineCount = int(input('how many queries:'))
            queries = []
            for i in range(lineCount):
                queries.append(input('record %d ' % (i + 1)))
        return (backload_urls, queries)


if __name__ == '__main__':
    solution = Solution()
    if len(sys.argv) == 3 and sys.argv[1] == '-f':
        file = open(sys.argv[2], 'r')
        solution.matchQuery(file)
        file.close()
    else:
        solution.matchQuery()
