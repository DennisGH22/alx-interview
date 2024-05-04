#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes:  A list of lists where each sublist represents a box
                and contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
