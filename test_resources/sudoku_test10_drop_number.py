import numpy as np
import random
from util import sudokufy as sudfy

random.seed(0)


def sudoku_drop_cell(sudoku_field, drop_cell):
    try:
        assert(0 <= drop_cell <= 81)
    except AssertionError:
        raise Exception("drop_cell must be set within (0, 81) inclusive!")

    flatten_sudoku = np.ravel(sudoku_field)
    empty_idx = random.sample(range(0, 81, 1), drop_cell)
    for i in empty_idx:
        flatten_sudoku[i] = 0

    return sudfy.sudokufy(flatten_sudoku)
