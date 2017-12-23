from collections import Counter


class Earn_and_Delete:
    def solve(self, nums):
        countDict = Counter(nums)
        setLt = list(set(nums))
        return self.dp(setLt, countDict)

    def dp(self, setLt, numCountDict):
        if len(setLt) == 0:
            return 0
        nonSelectSum = self.dp(setLt[1:], numCountDict)
        
        if setLt[0] + 1 in setLt:
            selectSum = numCountDict[setLt[0]] * \
                setLt[0] + self.dp(setLt[2:], numCountDict)
        else:
            selectSum = numCountDict[setLt[0]] * \
                setLt[0] + nonSelectSum

        return max(selectSum, nonSelectSum)


if __name__ == '__main__':
    print(Earn_and_Delete().solve([1, 2, 3, 3, 4, 4, 5]))
    print(Earn_and_Delete().solve([1, 2, 3, 4, 5]))
