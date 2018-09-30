class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        result = '#'
        for i in range(3):
            s = int(color[i * 2 + 1: i * 2 + 3], 16)
            d = (s // 17) * 17
            if d + 17 - s < s - d:
                result += hex(d + 17)[2:]
            else:
                t = hex(d)[2:]
                result += t if len(t) == 2 else t * 2
        return result


if __name__ == '__main__':
    print(Solution().similarRGB('#001122'))
    print(Solution().similarRGB('#334455'))
    print(Solution().similarRGB('#F03456'))
