class Name_Sort:
    def __init__(self):
        self.charDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    def solve(self, names):
        return sorted(names, key=self.keyFunction)

    def keyFunction(self, str):
        if ' ' in str:
            tmpStrLt = str.split(' ')
            return (tmpStrLt[0], self.romeStrToNum(tmpStrLt[1]))
        else:
            return (str, 0)

    def romeStrToNum(self, str):
        i = 0
        result = 0
        while i < len(str):
            cv = self.charDict[str[i]]
            if i + 1 < len(str):
                nv = self.charDict[str[i + 1]]
                if cv < nv:
                    result += nv - cv
                    i += 2
                else:
                    result += cv
                    i += 1
            else:
                result += cv
                i += 1
        return result


if __name__ == '__main__':
    print(Name_Sort().solve(
        ['ABc', 'Abc', 'ABC', 'ABC I',
         'ABC II', 'ABC IV', 'ABC III',
         'ABC VI', 'ABC V', 'ABC VII', 'ABC VIII', 'ABC IX', 'ABC X']))
    print(Name_Sort().romeStrToNum('VII'))
    print(Name_Sort().romeStrToNum('CVI'))