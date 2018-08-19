from collections import Counter


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sc = Counter(S)
        result = 0
        for j in J:
            if j in sc:
                result += sc[j]

        return result


if __name__ == '__main__':
    print(Solution().numJewelsInStones('z', 'ZZ'))
    print(Solution().numJewelsInStones('z', 'ZZz'))
