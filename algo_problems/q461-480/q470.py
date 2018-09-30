# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 0
        while True:
            idx = rand7() + (rand7() - 1) * 7
            if idx <= 40:
                break
        return (idx % 10) + 1
