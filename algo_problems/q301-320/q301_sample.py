class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        rslt = []
        self.greedy(s, 0, 0 ,rslt, ['(', ')'])
        return rslt
    
    def greedy(self, word, last_j, last_i, rslt, p):
        cnt = 0
        print(word)
        for i in range(last_i, len(word)):
            if word[i] == p[0]:
                cnt += 1
            elif word[i] == p[1]:
                cnt -= 1
            if cnt < 0:
                for j in range(last_j, i+1):
                    if word[j] == p[1] and (j == last_j or word[j-1] != word[j]):
                        self.greedy(word[:j] + word[j+1:], j, i, rslt, p)
                return
        if p[0] == '(':
            self.greedy(word[::-1], 0, 0, rslt, [')', '('])
        else:
            rslt.append(word[::-1])
            
            
            

if __name__ == '__main__':
    print(Solution().removeInvalidParentheses('()())()'))