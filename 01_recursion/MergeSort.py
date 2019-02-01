import random


def MergeSort(arr, first, last):
    if last - first > 0:
        m = (first + last) // 2
        MergeSort(arr, first, m)
        MergeSort(arr, m + 1, last)
        Merge(arr, first, last, m)


def mergeSort(arr):
    first = 0
    last = len(arr) - 1
    MergeSort(arr, first, last)


def Merge(arr, first, last, m):
    n = last - first + 1
    b = [0] * n
    i = first
    j = m + 1
    for k in range(n):
        if j >= last + 1:
            b[k] = arr[i]
            i += 1
        elif i >= m + 1:
            b[k] = arr[j]
            j += 1
        elif arr[i] < arr[j]:
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
    for k in range(n):
        arr[k + first] = b[k]


if __name__ == '__main__':
    arr = [5, 18, 2, 40, 2, 62, 7, 9, 15, 14, 30, 21]
    mergeSort(arr)
    arr1 = sorted(arr)
    print(arr1 == arr)

    l = [random.randint(10, 5000) for _ in range(20000)]
    print(l)
    l1 = sorted(l)
    mergeSort(l)
    print(l == l1)
