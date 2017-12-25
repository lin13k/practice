class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ''
        if n == 0 or k <= 0:
            return result

        offsetK = k - 1
        charList = [str(i) for i in range(1, n + 1)]

        multiple = 1
        for i in range(2, n + 1):
            multiple *= i

        while len(charList) > 0:
            multiple /= len(charList)
            result += charList.pop(int(offsetK // multiple))
            offsetK = offsetK % multiple
        return result

if __name__ == '__main__':
    print(Solution().getPermutation(3, 4))
