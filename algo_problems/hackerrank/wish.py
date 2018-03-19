#!/bin/python3

import sys
import os
from collections import Counter

def numberOfPairs(a, k):
    c = Counter(a)
    result = 0
    for key in c:
        d = k - key
        if d in c and d != key:
            result += 0.5
        if d == key and c[key] >= 2:
            result += 1
    return int(result)


if __name__ == '__main__':
    print(numberOfPairs([1, 3, 46, 1, 3, 9], 47))
    print(numberOfPairs([6, 6, 3, 9, 3, 5, 1], 12))
