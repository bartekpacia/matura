from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    narr = arr.copy()
    length = len(narr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if narr[j] > narr[j + 1]:
                narr[j], narr[j + 1] = narr[j + 1], narr[j]

    return narr


def merge_sort(arr: List[int]) -> List[int]:
    pass


def insertion_sort(arr: List[int]) -> List[int]:
    pass


def quick_sort(arr: List[int]) -> List[int]:
    pass


def bucket_sort(arr: List[int]) -> List[int]:
    pass
