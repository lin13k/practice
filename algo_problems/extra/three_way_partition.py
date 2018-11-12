from statistics import median


def three_way_partition(arr):
    print(arr)
    mid = median(arr)
    i = j = 0
    k = len(arr) - 1
    while j <= k:
        if arr[j] < mid:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > mid:
            arr[k], arr[j] = arr[j], arr[k]
            k -= 1
        else:
            j += 1
    print(arr)


if __name__ == '__main__':
    three_way_partition([1, 5, 2, 3, 4, 6, 8, 7])

    three_way_partition([1, 2, 3, 2, 2, 1, 9])
