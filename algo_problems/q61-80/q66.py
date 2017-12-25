class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        incrementFlag = True

        for i in range(len(digits)-1, -1, -1):
            if incrementFlag:
                digits[i] += 1
                incrementFlag = False
                if digits[i] >= 10:
                    digits[i] %= 10
                    incrementFlag = True
            else:
                break

        if incrementFlag:
            digits = [1] + digits

        return digits

if __name__ == '__main__':
    print(Solution().plusOne([1,5,8,9,9,9]))