class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        upper_bound = 2147483647
        lower_bound = -2147483648
        tmpStr = str(x)
        if tmpStr[0] == '-':
            tmpN = -(int(tmpStr[-1:0:-1]))
        else:
            tmpN = int(tmpStr[::-1])
        if tmpN > upper_bound or tmpN < lower_bound:
            return 0
        return tmpN



if __name__ == '__main__':
    print(Solution().reverse(123), 321)
    print(Solution().reverse(-123), -321)