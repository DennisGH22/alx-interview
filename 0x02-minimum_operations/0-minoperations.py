#!/usr/bin/python3
"""
Calculates the fewest number of operations needed.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed,
             or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    min_operations_needed = [float('inf')] * (n + 1)
    min_operations_needed[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                min_operations_needed[i] = min(
                    min_operations_needed[i],
                    min_operations_needed[j] + i // j)

    return min_operations_needed[n] if (
        min_operations_needed[n] != float('inf')) else 0
