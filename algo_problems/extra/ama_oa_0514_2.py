import re


class Solution:
    def __init__(self, input_strings):
        self.lines = input_strings.split('\n')

    def sortedLines(self):
        def keyFunc(line):
            print(line)
            try:
                value = re.findall(r'[\w]+', line)[1]
            except Exception as e:
                raise Exception('not valid line:' + line)

            if len(re.findall(r'[\d]+', value)) > 0:
                return '{'
            return value

        return sorted(self.lines, key=keyFunc)


if __name__ == '__main__':
    print(Solution(
        '''mi2 jog mid pet
wz3 34 54 398
al alps cow bar
x4 45 21 7'''
    ).sortedLines())

    print(Solution(
        '''line1 Zz xxxxxx
line2 zZ xxxxxx
line3 1321 xxxxxx
line4 14 xxxxxx
line5 12 xxxxxx
line6 aa xxxxxx'''
    ).sortedLines())
