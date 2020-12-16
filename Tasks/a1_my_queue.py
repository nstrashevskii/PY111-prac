"""
My little Queue
"""
from typing import Any

my_queue = []  # конец очереди слева


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.insert(0, elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if not my_queue:
        return None
    else:
        return my_queue.pop()


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind > len(my_queue) or ind < 0:
        return None
    else:
        print(my_queue[-1 - ind])
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None


if __name__ == '__main__':
    enqueue(1)
    enqueue(2)
    print(peek(12))