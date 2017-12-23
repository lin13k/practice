def buildKmpTable(s):
    i = 1
    j = 0
    result = [0]
    while i < len(s):
        if s[j] == s[i]:
            result.append(j + 1)
            i += 1
            j += 1
        elif j > 0:
            j = result[j - 1]
        else:
            result.append(0)
            i += 1
    return result


def partial(pattern):
    """ Calculate partial match table: String -> [Int]"""
    ret = [0]

    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret


def kmpTable(s):
    result = [0]
    for i in range(1, len(s)):
        j = result[i - 1]
        while j > 0 and s[i] != s[j]:
            j = result[j - 1]
        if s[i] == s[j]:
            result.append(j + 1)
        else:
            result.append(j)
    return result


def searchByKmp(s, w):
    kmp = kmpTable(s)
    j = 0
    result = []
    for i in range(len(s)):
        while j > 0 and w[j] != s[i]:
            j = kmp[j - 1]
        if w[j] == s[i]:
            j += 1
        if j == len(w):
            result.append(i - j + 1)
            j = 0
    return result


if __name__ == '__main__':
    print(buildKmpTable('abcdabca'))
    print(partial('abcdabca'))
    print(kmpTable('abcdabca'))
    print(buildKmpTable('abcdabce'))
    print(partial('abcdabce'))
    print(kmpTable('abcdabce'))

    # print(searchByKmp('abcdabceababcab', 'ab'))    
    # print(searchByKmp('abcdabceababcab', 'abc'))    
