import numpy as np


def sudokufy(sudoku_field):
    try:
        assert(type(sudoku_field) == np.ndarray)
        if len(sudoku_field.shape) == 1:
            assert(sudoku_field.shape[0] == 81)
        else:
            assert(sudoku_field.shape[0]*sudoku_field.shape[1] == 81)
        print(len(sudoku_field.shape))
        assert(len(sudoku_field.shape) <= 2)
    except AssertionError:
        raise Exception("Argument is not 2D ndarray and/or its doesnt have exactly 81 elements!")
    ravel_sudoku = np.reshape(np.ravel(sudoku_field), (9, 9))
    return ravel_sudoku

