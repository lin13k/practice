MAP = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution(object):
    def letterCombinations(self, digits):
        counterList = [0] * len(digits)
        result = []
        while counterList:
            tmpStr = ''
            for i in range(len(counterList)):
                tmpStr += MAP[digits[i]][counterList[i]]
            result.append(tmpStr)
            counterList = self.increaseCounter(counterList, digits, 0)
        return result

    def increaseCounter(self, counterList, digits, pos):
        if pos >= len(digits):
            return None
        if counterList[pos] + 1 >= len(MAP[digits[pos]]):
            counterList[pos] = 0
            return self.increaseCounter(counterList, digits, pos + 1)
        else:
            counterList[pos] += 1
            return counterList


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
    print(Solution().letterCombinations('2323'))