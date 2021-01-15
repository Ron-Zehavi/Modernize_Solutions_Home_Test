#!/usr/bin/python3

from puzzle import Puzzle
import sys

if __name__ == '__main__':
    puzzle = Puzzle()
    user_input = ''
    while not puzzle.is_solved():
        print(puzzle)
        movable_tiles = puzzle.get_valid_tiles_for_swap()
        user_input = input(f'\tPlease enter piece number to swap {movable_tiles} or enter x to exit - ')
        if user_input.lower() == 'x':
            print("\n\tSo Long, and Thanks for All the Fish")
            sys.exit()
        elif puzzle.check_input(user_input):
            puzzle.swap(user_input)
    print(puzzle)
    print("\nCONGRATS!\nYou are the CHAMPION my friend")
