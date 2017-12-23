class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a) - 1
        n2 = len(b) - 1
        result = ''
        addToNext = False
        while n1 >= 0 or n2 >= 0:
            tmpValue = 0
            if n1 >= 0:
                tmpValue += 0 if a[n1] == '0' else 1
            if n2 >= 0:
                tmpValue += 0 if b[n2] == '0' else 1
            if addToNext:
                tmpValue += 1

            if tmpValue >= 2:
                addToNext = True
            else:
                addToNext = False
            if tmpValue % 2 == 1:
                result = '1' + result
            else:
                result = '0' + result
            n1 -= 1
            n2 -= 1
        if addToNext is True:
            result = '1' + result
        return result
