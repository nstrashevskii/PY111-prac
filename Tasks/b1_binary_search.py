from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if not arr:
        return None

    arr_l = arr[:]
    left_index = 0
    right_index = len(arr_l) - 1

    while left_index < right_index:
        if arr_l[left_index] == elem:
            return left_index
        elif arr_l[right_index] == elem:
            while arr_l[right_index - 1] == elem:
                right_index -= 1
            return right_index

        middle_index = left_index + (right_index - left_index) // 2
        if arr_l[middle_index] == elem:
            while arr_l[middle_index - 1] == elem:
                middle_index -= 1
            return middle_index

        elif arr_l[middle_index] < elem:
            left_index = middle_index + 1
        elif arr_l[middle_index] > elem:
            right_index = middle_index - 1

    return None

