def bubble_sort(a: list[int], debug=False) -> list[int]:
    """
    Time complexity: O(n^2)
    """
    if debug:
        print("bubble sort")

    arr = a.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                if debug:
                    print(i, arr)

    return arr


def insertion_sort(a: list[int], debug=False) -> list[int]:
    """
    Time complexity: O(n^2)
    """
    if debug:
        print("insertion sort")

    arr = a.copy()
    n = len(arr)
    for i in range(1, n):
        el = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > el:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = el

        if debug:
            print(i, arr)

    return arr


def selection_sort(a: list[int], debug=False) -> list[int]:
    """
    Time complexity: O(n^2)
    """
    if debug:
        print("selection sort")

    arr = a.copy()
    n = len(arr)
    for i in range(n):
        index_min = i
        for j in range(index_min + 1, n):
            if arr[j] < arr[index_min]:
                index_min = j

        arr[i], arr[index_min] = arr[index_min], arr[i]
        if debug:
            print(i, arr)

    return arr


def merge_sort(
    arr: list[int], left_index: int = None, right_index: int = None
) -> list[int] | None:
    if not left_index:
        left_index = 0

    if not right_index:
        right_index = len(arr) - 1

    if left_index >= right_index:
        print("something is wrong")
        return None

    middle = (left_index + right_index) // 2
    merge_sort(arr, left_index, middle)
    merge_sort(arr, middle + 1, right_index)
    merge(arr, left_index, right_index, middle)

    return arr


def merge(arr: list[int], left_index: int, right_index: int, middle: int):
    # Make copies of both arrays we're trying to merge
    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = arr[left_index : middle + 1]
    right_copy = arr[middle + 1 : right_index + 1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


def bucket_sort(arr: list[int]) -> list[int]:
    pass
