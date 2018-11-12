class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        m = len(A[0])
        visit = [[0 for j in range(m)] for i in range(n)]
        result = 0
        q = []
        i = j = 0
        found = False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while i < n and found is False:
            while j < m and found is False:

                if A[i][j] == 1:
                    q.append((i, j))
                    while len(q) > 0:
                        x, y = q.pop(0)
                        v = A[x][y]
                        for dx, dy in directions:
                            tmpx = x + dx
                            tmpy = y + dy
                            if (0 <= tmpx <= n and
                                    0 <= tmpy <= m):
                                if A[tmpx][tmpy] == 1 and visit[tmpx][tmpy] == 0:
                                    
                j += 1
            i += 1


if __name__ == '__main__':
    print(Solution().shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
          1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
