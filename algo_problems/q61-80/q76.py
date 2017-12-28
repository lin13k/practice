from collections import Counter


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        need = Counter(t)
        start = 0
        end = 0
        n = len(s)
        result = ''
        count = len(need)
        while end < len(s):
            if s[end] not in need:
                end += 1
                continue
            need[s[end]] -= 1
            if need[s[end]] == 0:
                count -= 1
            if count == 0:
                while start < end + 1:
                    if s[start] in need:
                        need[s[start]] += 1
                        if need[s[start]] > 0:
                            count += 1
                            if n > end - start:
                                result = s[start: end + 1]
                                n = end - start
                            start += 1
                            break
                    start += 1
            end += 1
        return result


if __name__ == '__main__':
    print(Solution().minWindow('aabcd', 'abc'))
