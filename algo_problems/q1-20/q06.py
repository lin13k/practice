class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        sectionN = numRows * 2 - 2
        result = [[] for i in range(numRows)]
        for i in range(len(s)):
            tmpN = i % sectionN
            if tmpN < numRows:  # straight down
                result[tmpN].append(s[i])
            else:  # goes to right up
                result[numRows - tmpN - 2].append(s[i])
        return ''.join([''.join(row) for row in result])


if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')