class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        carryFlag = True
        for i in range(len(digits) - 1, -1, -1):
            if carryFlag:
                digits[i] += 1
                carryFlag = digits[i] >= 10
                digits[i] %= 10
            else:
                break
        if carryFlag:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    print(Solution().plusOne([1, 3, 4, 9, 9]))
    print(Solution().plusOne([9]))
