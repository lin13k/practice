class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        found_1_flag = False
        pos_1 = None
        pos_0 = None
        i = 0
        while i < 32:
            if n >> i & 1 == 1:
                found_1_flag = True
                pos_1 = i
            else:
                if found_1_flag is True:
                    pos_0 = i

            if pos_0 is not None and pos_1 is not None:
                return n - (1 << pos_1) + (1 << pos_0)

            i += 1

        return -1


def printIntAsDigits(n):
    result = []
    for i in range(32):
        if 1 & n >> i == 1:
            result.insert(0, '1')
        else:
            result.insert(0, '0')

    return ''.join(result)


if __name__ == '__main__':
    print(printIntAsDigits(12))
    print(printIntAsDigits(20))
    print(printIntAsDigits(21))
    # print(printIntAsDigits(128))
    print(Solution().nextGreaterElement(12))
    # print(Solution().nextGreaterElement(128))
