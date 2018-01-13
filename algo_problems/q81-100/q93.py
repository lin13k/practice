class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.findAddress(s, [], result)
        return result

    def findAddress(self, s, path, result):
        if len(path) == 4 and len(s) != 0:
            return
        if len(path) == 4 and len(s) == 0:
            result.append('.'.join(path))
        if len(s) == 0:
            return

        self.findAddress(s[1:], path + [s[0]], result)
        if s[0] != '0':
            if len(s) >= 2:
                self.findAddress(s[2:], path + [s[:2]], result)
            if len(s) >= 3 and int(s[:3]) < 256:
                self.findAddress(s[3:], path + [s[:3]], result)


if __name__ == '__main__':
    print(Solution().restoreIpAddresses('19216801'))
