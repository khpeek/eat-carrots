import itertools
from typing import List, Tuple, Optional


def eat_carrots(garden: List[List[int]]) -> int:
    """
    Return the total number of carrots eaten by a bunny who starts in the middle
    of the garden at the cell with the most carrots and eats all the carrots in
    each cell, moving to the next cell with the most carrots, until none of the
    adjacent cells contain any carrots
    """
    cell = get_center_cell(garden)
    carrots_eaten = 0

    while cell:
        i, j = cell
        carrots_eaten += garden[i][j]   # Increment the total number of carrots eaten
        garden[i][j] = 0                # Set the number of carrots in the visited cell to zero

        # Get the next cell. When none of the adjacent cells contain any carrots,
        # this will return None and terminate the while loop on the next iteration
        cell = get_next_cell(cell, garden)

    return carrots_eaten


def carrots(cell: Tuple[int, int], garden: List[List[int]]) -> int:
    # Convenience method for obtaining the number of carrots at a given cell
    i, j = cell
    return garden[i][j]


def get_next_cell(cell: Tuple[int, int], garden: List[List[int]]) -> Optional[Tuple[int, int]]:
    """
    Get the adjacent cell containing the most carrots. If none of the adjacent
    cells contain carrots, return None.
    """
    next_cell = max(get_adjacent_cells(cell, garden), key=lambda cell: carrots(cell, garden))
    return next_cell if carrots(next_cell, garden) > 0 else None


def get_adjacent_cells(cell: Tuple[int, int], garden: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Get a list of adjacent cells, taking into account the boundaries of the garden
    """
    i, j = cell
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [neighbor for neighbor in neighbors if in_bounds(neighbor, garden)]


def in_bounds(cell: Tuple[int, int], garden: List[List[int]]) -> bool:
    """
    Return a Boolean indicating whether a given coordinate is within the garden
    """
    i, j = cell
    return 0 <= i < len(garden) and 0 <= j < len(garden[0])


def get_center_cell(garden: List[List[int]]) -> Tuple[int, int]:
    """
    Get the cell in the center of the garden containing the most carrots
    """
    return max(
        get_center_cells(garden),
        key=lambda cell: carrots(cell, garden))


def get_center_cells(garden: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Return a list of cells in the center of the garden from the Cartesian
    product of the center coordinates in each dimension
    """
    return list(itertools.product(
        get_middle(len(garden)),
        get_middle(len(garden[0]))))


def get_middle(n: int) -> List[int]:
    """
    Given the length of one dimension of the garden, return the middle coordinates
    For even (odd) length dimensions there will be two (one) coordinate(s)
    """
    if n % 2 == 0:
        return [n//2 - 1, n//2]
    else:
        return [n//2]
