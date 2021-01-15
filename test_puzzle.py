from main import Puzzle
import numpy as np


def test_generate_start_position():
    # Arrange
    puzzle = Puzzle()
    # Act
    start_position = puzzle._generate_start_position()
    # Assert - Should generate 4*4 array with all numbers in range 0-15
    assert start_position.shape == (4, 4)

    for i in range(16):
        assert i in start_position


def test_generate_end_position():
    # Arrange
    puzzle = Puzzle()
    # Act
    end_position = puzzle._generate_end_position()
    # Assert - Should generate the solved position of the puzzle
    expected_end_position = np.array([[1, 2, 3, 4],
                                      [5, 6, 7, 8],
                                      [9, 10, 11, 12],
                                      [13, 14, 15, 0]])
    assert np.array_equal(end_position, expected_end_position)


def test_is_solved__solved():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
    # Assert - return True for solved puzzle
    assert puzzle.is_solved()


def test_is_solved__not_solved():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[2, 1, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
    # Assert - return False for unsolved puzzle
    assert not puzzle.is_solved()


def test_get_valid_tiles_for_swap__right_bottom():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
    # Act
    valid_tiles = puzzle.get_valid_tiles_for_swap()
    # Assert
    assert valid_tiles == [15, 12]


def test_get_valid_tiles_for_swap__middle():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[1, 2, 3, 4],
                                [5, 6, 0, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 7]])
    # Act
    valid_tiles = puzzle.get_valid_tiles_for_swap()
    # Assert
    assert valid_tiles == [6, 3, 8, 11]


def test_get_valid_tiles_for_swap__top_left():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[0, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 1]])
    # Act
    valid_tiles = puzzle.get_valid_tiles_for_swap()
    # Assert
    assert valid_tiles == [2, 5]


def test_swap():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
    # Act
    puzzle.swap(4)
    # Assert
    expected_swapped = np.array([[1, 2, 3, 0],
                                 [5, 6, 7, 8],
                                 [9, 10, 11, 12],
                                 [13, 14, 15, 4]])

    assert np.array_equal(puzzle.position, expected_swapped)


def test_get_coordinates():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
    # Assert
    assert puzzle._get_coordinates(1) == (0, 0)
    assert puzzle._get_coordinates(4) == (0, 3)
    assert puzzle._get_coordinates(13) == (3, 0)
    assert puzzle._get_coordinates(0) == (3, 3)


def test_swap_by_coordinates():
    # Arrange
    puzzle = Puzzle()
    puzzle.position = np.array([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
    # Act
    puzzle._swap_by_coordinates(0, 0, 1, 1)
    # Assert
    expected_swapped = np.array([[6, 2, 3, 4],
                                  [5, 1, 7, 8],
                                  [9, 10, 11, 12],
                                  [13, 14, 15, 0]])
    assert np.array_equal(puzzle.position, expected_swapped)
