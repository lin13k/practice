from collections import Counter


class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        s = sum(nums)
        equalLen = s // 4
        if equalLen * 4 != s:
            return False

        if len(nums) < 4:
            return False

        if nums[-1] > equalLen:
            return False
        self.sset = set()
        countDict = Counter(nums)
        return self.helper(countDict, 3, equalLen, equalLen)

    def helper(self, countDict, times, leftValue, equalLen):
        if times == 0 and\
                all(c == 0 for c in countDict.values()) and leftValue == 0:
            return True

        if leftValue == 0:
            leftValue = equalLen
            times -= 1

        for key in countDict:
            if key <= leftValue and\
                    countDict[key] > 0 and\
                    (times, leftValue - key) not in self.sset:
                countDict[key] -= 1
                result = False
                if (tuple(countDict.values()),
                        times, leftValue - key) not in self.sset:
                    result = self.helper(
                        countDict, times, leftValue - key, equalLen)
                if result:
                    return True
                else:
                    self.sset.add((tuple(countDict.values()), times, leftValue - key))
                countDict[key] += 1

        return False


if __name__ == '__main__':
    print(Solution().makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))
