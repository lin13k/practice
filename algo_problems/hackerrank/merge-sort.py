#!/bin/python3

import sys


def countInversions(arr):
    countNumber = 0
    if len(arr) < 2:
        return 0

    
    def top_down_merge(arr1, arr2):
        result = {}
        if len(arr1) == 0 or len(arr2) == 0:
            return arr1 + arr2

        arr1 = top_down_merge(arr1[:len(arr1) // 2], arr1[len(arr1) // 2:])
        arr2 = top_down_merge(arr2[:len(arr2) // 2], arr2[len(arr2) // 2:])

        while len(arr1) > 0:
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
                countNumber += len(arr1)
        return result

    top_down_merge(arr[:len(arr) // 2], arr[len(arr) // 2:])
    return countNumber


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
