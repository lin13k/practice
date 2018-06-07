import re
from collections import Counter


class Solution():

    def __init__(self, input_string, exclude_list):
        self.input_string = input_string.lower()
        self.exclude_list = exclude_list

    def findMostAppearedWords(self):
        words = re.findall(r'[\w]+', self.input_string)
        d = Counter(words)
        # sd = sorted(d.items(), key=lambda x: x[1])
        for key in self.exclude_list:
            d.pop(key)
        print(d)
        maxValue = max(d.values())
        result = []
        for item in d.items():
            if item[0] not in self.exclude_list and item[1] == maxValue:
                result.append(item[0])
        return result


if __name__ == '__main__':
    print(Solution('rose is a flower rose is pond a flower rose flower in garden garden garden pond pond rose is a rose is a rose is a rose', ['rose']).findMostAppearedWords())
    print(Solution("abc abc ab's ab's", ['abc']).findMostAppearedWords())
    print(Solution("abc abc\"s ab's ab'\"s", ['abc']).findMostAppearedWords())
