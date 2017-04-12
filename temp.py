

def oddFilter(inputList):
    result = []
    for i in range(len(inputList)):
        if inputList[i] % 2 != 0:
            result.append(inputList[i])
    return result


if __name__ == '__main__':
    x = [5, 6, 8, 1, 2, 3, 7, 9, 4, 0]
    print(oddFilter(x))
