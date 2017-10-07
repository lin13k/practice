#!/bin/python3
from heapq import (
    heappop, heappush
)


n = int(input().strip())
a = []
a_i = 0
heapLt = []
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)

    heappush(heapLt, a[-1])

    tmpLt = heapLt[:]

    result = 0
    if a_i % 2 == 0:
        for i in range(a_i // 2 + 1):
            result = heappop(tmpLt)
    else:
        for i in range(a_i // 2 + 1):
            result = heappop(tmpLt)
        result = (result + heappop(tmpLt)) / 2.0

    print('%.1f' % result)
