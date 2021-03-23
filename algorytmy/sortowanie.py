from typing import List


def bubble_sort(a: List[int]) -> List[int]:
    arr = a.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(a: List[int]) -> List[int]:
    arr = a.copy()
    n = len(arr)
    for i in range(1, n):
        el = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > el:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = el

    return arr


def selection_sort(a: List[int]) -> List[int]:
    arr = a.copy()
    n = len(arr)
    for i in range(n):
        index_min = i
        for j in range(index_min + 1, n):
            if arr[j] < arr[index_min]:
                index_min = j

        arr[i], arr[index_min] = arr[index_min], arr[i]

    return arr

def merge_sort(a: List[int]) -> List[int]:
    pass


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


def bucket_sort(arr: List[int]) -> List[int]:
    pass
