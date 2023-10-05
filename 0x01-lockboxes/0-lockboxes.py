#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    """Initialize a list to keep track of visited boxes"""
    visited = [False] * len(boxes)
    visited[0] = True  """The first box is unlocked by default"""
    queue = [0]  """Start with the first box in the queue"""

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if key >= 0 and key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)

    """ Check if all boxes have been visited"""
    return all(visited)
