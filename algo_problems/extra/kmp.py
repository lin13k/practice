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

if __name__ == '__main__':
    print(buildKmpTable('abcdabca'))
