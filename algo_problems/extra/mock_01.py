"""
input "AB"
output ["AB", "Ab", "aB", "ab"] 
"""


def solution(in_str):
    result = []
    recursiveSearch('', in_str, result)
    return result


def recursiveSearch(prefix, surfix, result):
    if len(surfix) == 0:
        result.append(prefix)
    else:
        tmpChar = surfix[0]
        recursiveSearch(prefix + tmpChar.upper(), surfix[1:], result)
        recursiveSearch(prefix + tmpChar.lower(), surfix[1:], result)


if __name__ == '__main__':
    print(solution('AA'))
    print(solution('AABc'))
    print(solution('AAcB'))
