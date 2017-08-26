class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                value = int(num1[i]) * int(num2[j])
                if i + j > len(result) - 1:
                    result.append(value)
                else:
                    result[j + i] += value

        for i in range(len(result)):
            v = result[i]
            result[i] = v % 10
            if i + 1 < len(result):
                result[i + 1] += v // 10
            else:
                if v // 10 > 0:
                    result.append(v // 10)

        tmp = ''.join([str(i) for i in result[::-1]])

        import re
        if re.match('^0*$', tmp):
            return '0'

        return tmp


if __name__ == '__main__':
    print(Solution().multiply('11', '11'))
    print(Solution().multiply('9', '8'))
    print(Solution().multiply('12345', '1'))
    print(Solution().multiply('0', '11'))