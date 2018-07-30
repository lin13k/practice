class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        sset = set(stones)
        done = set()

        def hop(curr, k):
            if curr == stones[-1]:
                return True
            if k < 1 or curr not in sset or (curr, k) in done:
                return False
            done.add((curr, k))
            return (hop(curr + k - 1, k - 1) or
                    hop(curr + k, k) or
                    hop(curr + k + 1, k + 1))

        return hop(1, 1)


if __name__ == '__main__':
    print(Solution().canCross(
        [0, 1, 3, 5]))
    print(Solution().canCross(
        [0, 1, 3, 5, 6, 8, 12, 17]))
    print(Solution().canCross(
        [0, 1, 2, 3, 4, 8, 9, 11]))
    print(Solution().canCross(
        [0, 1, 3, 4, 5, 7, 9, 10, 12]))
