class Solution(object):
    def firstMissingPositive(self, nums):
        total = 0
        count = 0
        minValue = None
        for i in nums:
            if i > 0:
                if not minValue:
                    minValue = i
                count += 1
                total += i
                minValue = min(i, minValue)

        if minValue != 1:
            return 1

        return (count + 1) * (count + 2) // 2 - total

if __name__ == '__main__':
    print(Solution().firstMissingPositive([1,2,0]))
    print(Solution().firstMissingPositive([3,4,-1,1]))
    print(Solution().firstMissingPositive([3,4,-1]))
