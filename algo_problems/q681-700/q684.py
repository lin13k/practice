class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [i for i in range(2001)]
        for edge in edges:
            if (self.find(parent, edge[0]) ==
                    self.find(parent, edge[1])):
                return edge
            parent[self.find(parent, edge[0])] = self.find(parent, edge[1])

    def find(self, parent, f):
        if parent[f] != f:
            parent[f] = self.find(parent, parent[f])
        return parent[f]


if __name__ == '__main__':
    print(Solution().findRedundantConnection([[1,2],[2,3],[1,3]]))