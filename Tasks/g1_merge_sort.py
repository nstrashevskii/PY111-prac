from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def _merge(left_container: List[int], right_container: List[int]) -> List[int]:
        current_elem_from_left_container = 0
        current_elem_from_right_container = 0
        merged_container = []

        for _ in range(len(left_container) + len(right_container) - 1):
            if left_container[current_elem_from_left_container] < right_container[current_elem_from_right_container]:
                merged_container.append(left_container[current_elem_from_left_container])
                current_elem_from_left_container += 1
            else:
                merged_container.append(right_container[current_elem_from_right_container])
                current_elem_from_right_container += 1
            if (current_elem_from_left_container + 1) > len(left_container):
                merged_container.extend(right_container[current_elem_from_right_container:])
                break
            elif (current_elem_from_right_container + 1) > len(right_container):
                merged_container.extend(left_container[current_elem_from_left_container:])
                break
        return merged_container

    if len(container) == 1:
        return container

    middle = len(container) // 2
    return _merge(sort(container[:middle]), sort(container[middle:]))
