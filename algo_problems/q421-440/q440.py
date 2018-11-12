class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 1
        k -= 1
        while k > 0:
            intv = [result, result + 1]
            cnt = 0
            while intv[0] <= n:
                cnt += min(intv[1], n + 1) - intv[0]
                intv = [intv[0] * 10, intv[1] * 10]

            if k >= cnt:
                k -= cnt
                result += 1
            else:
                k -= 1
                result *= 10
        return result


if __name__ == '__main__':
    print(Solution().findKthNumber(13, 2))
