class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        intPart = numerator // denominator
        path = []
        fraPart = numerator % denominator
        r = 0
        while True:
            r = fraPart * 10 // denominator
            if r in path:
                break
            path.append(r)
            fraPart = fraPart * 10 % denominator

        if len(path) == 0:
            return str(intPart)
        return str(intPart) + '.' + fraStr
