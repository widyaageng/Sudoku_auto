import numpy as np
import random
from test_resources import sudoku_test10_gen
from train_resource import sudoku_gen

random.seed(0)


def sudoku_drop_cell(sudoku_field, drop_cell):
    try:
        assert(0 <= drop_cell <= 81)
    except AssertionError:
        raise Exception("drop_cell must be set within (0, 81) inclusive!")

    try:
        assert(sudoku_field.shape == (9, 9, 10))
    except AssertionError:
        raise Exception("Input sudoku do not have 9-by-9 size and/or is not exactly 10 sudoku field")
    empty_idx = random.sample(range(0, 81, 1), drop_cell)
    for i in empty_idx:
        sudoku_field[divmod(i, 9)[0], divmod(i, 9)[1], :] = 0
    return sudoku_field


test_sud = sudoku_gen.sudoku_gen_init()
print(test_sud)
test_sud = sudoku_test10_gen.sudoku_test10_gen_init(test_sud)
print(test_sud)
# print(test_sud[:, :, 0])
# test_sud = sudoku_drop_cell(test_sud, 40)
# print(test_sud)
