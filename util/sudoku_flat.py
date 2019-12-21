import numpy as np


def flat_sudoku_to_col_vec(sudoku_field):
    try:
        assert (type(sudoku_field) == np.ndarray)
        if len(sudoku_field.shape) == 1:
            assert (sudoku_field.shape[0] == 81)
        else:
            assert (sudoku_field.shape[0] * sudoku_field.shape[1] == 81)
        print(len(sudoku_field.shape))
        assert (len(sudoku_field.shape) <= 2)
    except AssertionError:
        raise Exception("Argument is not 2D ndarray and/or its doesnt have exactly 81 elements!")
    temp_sudoku = np.ravel(sudoku_field)
    temp_sudoku = np.reshape(temp_sudoku, (81, 1))
    return temp_sudoku


def flat_sudoku_to_row_vec(sudoku_field):
    try:
        assert (type(sudoku_field) == np.ndarray)
        if len(sudoku_field.shape) == 1:
            assert (sudoku_field.shape[0] == 81)
        else:
            assert (sudoku_field.shape[0] * sudoku_field.shape[1] == 81)
        print(len(sudoku_field.shape))
        assert (len(sudoku_field.shape) <= 2)
    except AssertionError:
        raise Exception("Argument is not 2D ndarray and/or its doesnt have exactly 81 elements!")
    temp_sudoku = np.ravel(sudoku_field)
    temp_sudoku = np.reshape(temp_sudoku, (1, 81))
    return temp_sudoku
