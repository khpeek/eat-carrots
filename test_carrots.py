from typing import List
import pytest
from carrots import (
    eat_carrots,
    get_middle,
    get_center_cells,
    get_center_cell,
    in_bounds,
    get_adjacent_cells,
    get_next_cell)


@pytest.fixture
def garden() -> List[List[int]]:
    return [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8]]


def test_eat_carrots(garden) -> None:
    assert eat_carrots(garden) == 27


def test_get_middle_even_length() -> None:
    assert get_middle(4) == [1, 2]


def test_get_middle_odd_length() -> None:
    assert get_middle(3) == [1]


def test_get_center_cells_four_by_four() -> None:
    garden = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

    # The 'center' consists of four cells
    assert get_center_cells(garden) == [(1, 1), (1, 2), (2, 1), (2, 2)]

def test_get_center_cells_three_by_three() -> None:
    garden = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

    # Since the garden is of odd length in both dimensions, the center
    # consists of a single cell
    assert get_center_cells(garden) == [(1, 1)]


def test_get_center_cells_three_by_four() -> None:
    garden = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

    assert get_center_cells(garden) == [(1, 1), (1, 2)]


def test_get_center_cell(garden) -> None:
    # The center cell for the given test fixture contains the value 7
    assert get_center_cell(garden) == (1, 2)


def test_get_center_cell_lower(garden) -> None:
    # If we change the value of an adjacent center cell to 9 (greater than 7),
    # the coordinates of the center cell change accordingly
    garden[2][2] = 9
    assert get_center_cell(garden) == (2, 2)


def test_get_center_cell_four_by_four() -> None:
    garden = [
        [0, 0, 0, 0],
        [0, 1, 2, 0],
        [0, 3, 4, 0],
        [0, 0, 0, 0]]

    # The cell with the most carrots among the four center cells is returned
    assert get_center_cell(garden) == (2, 2)


def test_in_bounds(garden) -> None:
    assert in_bounds((0, 0), garden) is True
    assert in_bounds((-1, 0), garden) is False
    assert in_bounds((2, 5), garden) is False


def test_get_adjacent_cells(garden) -> None:
    # Get adjacent cells in the corner, middle, and side of the board
    assert get_adjacent_cells((0, 0), garden) == [(1, 0), (0, 1)]
    assert get_adjacent_cells((1, 1), garden) == [(0, 1), (2, 1), (1, 0), (1, 2)]
    assert get_adjacent_cells((2, 4), garden) == [(1, 4), (3, 4), (2, 3)]


def test_get_next_cell(garden) -> None:
    assert get_next_cell((0, 0), garden) == (0, 1)  # Move from 5 -> 7
    assert get_next_cell((1, 2), garden) == (0, 2)  # Move from 7 -> 8


def test_get_next_cell_when_surrounded_by_zeros(garden) -> None:
    garden = [
        [0, 0, 0],
        [1, 0, 2]]

    assert get_next_cell((0, 1), garden) is None
