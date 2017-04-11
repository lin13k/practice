from collections import Counter
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
    def recursiveSearch(self, s):
        tmpList = [i for i in s]
        cd = Counter(tmpList)

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("asjrgapa"))