from collections import Counter


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = Counter(s)
        result = "".join(
            k[1] * k[0] for k in sorted(
                list((v, i) for i, v in d.items()), reverse=True))
        return result


if __name__ == '__main__':
    print(Solution().frequencySort('tree'))
