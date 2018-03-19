class Solution:
    def park_distance(self, bikes):
        if len(bikes) == 0:
            return 0
        bikes.sort()
        pre = bikes[0]
        maxDistance = 0
        for i in bikes[1:]:
            if i - pre > maxDistance:
                maxDistance = i - pre
            pre = i
        print(maxDistance)
        return maxDistance / 2


if __name__ == '__main__':
    assert(Solution().park_distance([5, -5]) == 5)
    assert(Solution().park_distance([5, 0, -5]) == 2.5)
    assert(Solution().park_distance([2, 3, 4]) == 0.5)
    assert(Solution().park_distance([5, 2, -5, -2]) == 2)
    assert(Solution().park_distance([0]) == 0)
    assert(Solution().park_distance([]) == 0)
