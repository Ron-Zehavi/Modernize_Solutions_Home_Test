import numpy as np


class Puzzle:
    def __init__(self, side=4):
        """
        :param side: board side size
        """
        self.side = side
        self.position = self._generate_start_position()
        self.END_POSITION = self._generate_end_position()

    def _generate_start_position(self):
        """
        generate starting point of the board -
        4x4 tiles board (2D numpy array), where 15 numbered tiles are initially placed
        in random order and where 16th tile is missing (randomly placed on the board)
        """
        return np.random.permutation(np.arange(self.side ** 2)).reshape(self.side, self.side)

    def _generate_end_position(self):
        """
        generate end point of the board -
        board (2D numpy array) including ordered tiles from 1 to 15,
        where tile number 1 is at the top left corner
        and empty one is at the bottom right corner.
        """
        return np.append(np.arange(1, self.side ** 2), [0]).reshape(self.side, self.side)

    def is_solved(self):
        """
        :returns true if puzzle is solved correctly,
                 or false otherwise
        """
        return np.array_equal(self.position, self.END_POSITION)

    def get_valid_tiles_for_swap(self):
        """
        :returns list of values of valid tiles for swap
        """
        x, y = self._get_coordinates(0)
        valid_tiles = []
        if y - 1 >= 0:  # left tile
            valid_tiles.append(self.position[x][y - 1])
        if x - 1 >= 0:  # upper tile
            valid_tiles.append(self.position[x - 1][y])
        if y + 1 < self.side:  # right tile
            valid_tiles.append(self.position[x][y + 1])
        if x + 1 < self.side:  # lower tile
            valid_tiles.append(self.position[x + 1][y])
        return valid_tiles

    def check_input(self, inp):
        """
        :returns True if input is valid
                 or printing adequate message for other case
                 and returning False
        """
        if not inp.isnumeric():
            print('\n\t Illegal input!!!')
            return False
        elif int(inp) not in range(self.side ** 2):
            print('\n\t Tile is out of the board!')
            return False
        elif int(inp) not in self.get_valid_tiles_for_swap():
            print(f"\n\t Tile {inp} can't move there")
            return False
        else:
            return True

    def swap(self, tile_num):
        """
        Swap the positions between chosen element and the empty tile (0)
        """
        empty_y, empty_x = self._get_coordinates(0)
        tile_y, tile_x = self._get_coordinates(int(tile_num))
        self._swap_by_coordinates(empty_y, empty_x, tile_y, tile_x)

    def _get_coordinates(self, tile):
        """
        Returns the i, j coordinates for a given tile
        """
        coordinates = np.where(self.position == tile)
        return coordinates[0][0], coordinates[1][0]

    def _swap_by_coordinates(self, x1, y1, x2, y2):
        """
        Swap the positions between two elements
        """
        self.position[x1][y1], self.position[x2][y2] = self.position[x2][y2], self.position[x1][y1]

    def __str__(self):
        """
        Print in console as a matrix
        """
        len_of_horizontal_line = self.side * 5 + 1
        horizontal_line = '     ' + ('-' * len_of_horizontal_line) + '\n    '
        puzzle_string = horizontal_line
        for i in range(self.side):
            for j in range(self.side):
                puzzle_string += ' │ {0: >2}'.format(str(self.position[i][j]))
                if j == self.side - 1:
                    puzzle_string += ' │\n'
                    puzzle_string += horizontal_line
        return puzzle_string
