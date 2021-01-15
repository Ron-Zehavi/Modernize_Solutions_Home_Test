import sys
from puzzle import Puzzle

EXIT_GAME_MESSAGE = "\n\tSo Long, and Thanks for All the Fish"
REQUEST_INPUT_MESSAGE = "\tPlease enter piece number to swap or enter x to exit -"
INVALID_INPUT_MESSAGE = "\tInvalid input"
GAME_WON_MESSAGE = "\nCONGRATS!\nYou are the CHAMPION my friend"


class GameEngine:
    def __init__(self, puzzle=Puzzle()):
        """
        :param puzzle: a puzzle class
        """
        self.puzzle = puzzle

    def __str__(self):
        return str(self.puzzle)

    def __handle_input(self, user_input):
        if user_input.lower() == 'x':
            print(EXIT_GAME_MESSAGE)
            sys.exit()

        is_valid, error = self.puzzle.validate_input(user_input)
        if is_valid:
            self.puzzle.swap(user_input)
        else:
            print(f'{INVALID_INPUT_MESSAGE} - {error}')

    def __is_game_won(self):
        return self.puzzle.is_solved()

    def start_game(self):
        while not self.__is_game_won():
            print(self)
            movable_tiles = self.puzzle.get_valid_tiles_for_swap()
            self.__handle_input(input(f'{REQUEST_INPUT_MESSAGE} ({movable_tiles})'))

        print(self)
        print(GAME_WON_MESSAGE)
