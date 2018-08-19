class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        headFlag = False
        headCnt = 0
        while i < len(data):
            if not headFlag:
                # find the head
                for j in range(7):
                    if data[i] >> (7 - j) & 1 == 1:
                        headCnt += 1
                    else:
                        break
                if headCnt == 1 or headCnt >= 5:
                    return False
                headFlag = True
                i += 1
            else:
                # find the following
                for j in range(headCnt - 1):
                    if i >= len(data) or not data[i] >> 6 == 2:
                        return False
                    i += 1
                headFlag = False
                headCnt = 0
            print(i, headFlag, headCnt)
        if headCnt == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().validUtf8([250, 145, 145, 145, 145]))
