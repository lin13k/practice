class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        tmpDivd = dividend
        quotient = 0
        mFlag = False if (tmpDivd > 0 and divisor > 0) or (
            tmpDivd < 0 and divisor < 0) else True
        tmpDivd = abs(tmpDivd)
        while tmpDivd >= abs(divisor):
            tmpDivr = abs(divisor)
            step = 1
            while tmpDivr < tmpDivd:
                tmpDivr = tmpDivr << 1
                step = step << 1

            if tmpDivd != tmpDivr:
                tmpDivd -= tmpDivr >> 1
                quotient += step >> 1
            else:
                tmpDivd -= tmpDivr
                quotient += step

        if mFlag:
            quotient = - quotient
        else:
            quotient = quotient
        if quotient > 2147483647:
            quotient = 2147483647
        elif quotient < -2147483648:
            quotient = -2147483648
        return quotient


if __name__ == '__main__':
    # print(Solution().divide(25, 7))
    # print(Solution().divide(25, -7))
    # print(Solution().divide(-25, 7))
    # print(Solution().divide(1, 1))
    print(Solution().divide(1, -1))
