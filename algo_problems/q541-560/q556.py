class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if s[i] > s[i - 1]:
                tmp = sorted(s[i - 1:])
                for j in range(len(tmp)):
                    if tmp[j] > s[i - 1]:
                        c = tmp.pop(j)
                        break
                r = int(s[:i - 1] + c + ''.join(tmp))
                return r if r < (1 << 31) - 1 else -1
        return -1


if __name__ == '__main__':
    # print(printIntAsDigits(12))
    # print(printIntAsDigits(20))
    # print(printIntAsDigits(21))
    # print(printIntAsDigits(128))
    print(Solution().nextGreaterElement(12))
    print(Solution().nextGreaterElement(12443322))
