from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sd = Counter(secret)
        gd = Counter(guess)
        aCount = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                aCount += 1
                sd[secret[i]] -= 1
                gd[secret[i]] -= 1

        bCount = 0
        for key, value in sd.items():
            if key in gd and gd[key] > 0:
                bCount += min(gd[key], value)

        return str(aCount) + 'A' + str(bCount) + 'B'


if __name__ == '__main__':
    print(Solution().getHint('1234', '2341'))
    print(Solution().getHint('1241', '2341'))
