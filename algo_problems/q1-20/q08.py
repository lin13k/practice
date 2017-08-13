class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        upper_bound = 2147483647
        lower_bound = -2147483648
        import re
        str = str.strip()
        m = re.search('^[-+]?[0-9]+', str)

        if not m:
            return 0
        else:
            if '+' in str[:m.start()] or '-' in str[:m.start()]:
                return 0
            tmpInt = int(m.group(0))
            if tmpInt > upper_bound:
                return upper_bound
            if tmpInt < lower_bound:
                return lower_bound
            return tmpInt