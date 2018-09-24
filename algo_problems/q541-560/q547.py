class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        if n == 1:
            return 1
        found = [False for i in range(n)]
        result = 0
        stack = []
        for i in range(n):
            if found[i] is True:
                continue
            result += 1
            stack.append(i)
            while len(stack) != 0:
                j = stack.pop()
                found[j] = True
                for k in range(n):
                    if found[k] is not True and M[j][k] == 1:
                        found[k] = True
                        stack.append(k)
        return result


if __name__ == '__main__':
    print(Solution().findCircleNum(
        [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1]
        ]
    ))
    print(Solution().findCircleNum(
        [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 1, 1]]
    ))
