class Solution(object):
    def generateParenthesis(self, n):
        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, left, right, prev, results):
        if left > right or left < 0 or right < 0:
            return
        if left == right and left == 0:
            results.append(prev)
            return
        if left == right:
            self.helper(left - 1, right, prev + '(', results)
        else:
            self.helper(left - 1, right, prev + '(', results)
            self.helper(left, right - 1, prev + ')', results)
