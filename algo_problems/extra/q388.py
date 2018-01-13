class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        data = input.split('\n')

        stack = []
        result = 0
        for i in range(len(data)):
            s = data[i]
            j = 0
            while s[j] == '\t':
                j += 1
            while len(stack) > j:
                stack.pop()
            isFile = '.' in s
            stack.append(s[j:])
            if isFile:
                result = max(result, len('-'.join(stack)))
        return result

if __name__ == '__main__':
    print(Solution().lengthLongestPath('dir\n\tabc\n\tdefg.png')) #dir-defg
