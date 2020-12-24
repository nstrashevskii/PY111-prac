def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    return n if n <= 1 else fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    n1 = 1
    n2 = 1
    if n < 0:
        raise ValueError

    if n < 2:
        return 1
    for i in range(2, n):
        n_sum = n1 + n2
        n1 = n2
        n2 = n_sum
    return n2
