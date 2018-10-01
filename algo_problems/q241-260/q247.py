class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)

    def helper(self, n, m):
        if n == 0:
            return ['']
        if n == 1:
            return ['1', '8', '0']
        preList = self.helper(n - 2, m)
        result = []
        for s in preList:
            if n != m:
                result.append('0' + s + '0')
            result.append('1' + s + '1')
            result.append('8' + s + '8')
            result.append('6' + s + '9')
            result.append('9' + s + '6')
        return result


if __name__ == '__main__':
    print(Solution().findStrobogrammatic(2))
    print(Solution().findStrobogrammatic(3))
