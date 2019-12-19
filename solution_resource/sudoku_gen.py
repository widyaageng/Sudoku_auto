import numpy as np
import random as ran


sudoku_array = []
ran.seed(0)
dump_num = 0


def sudoku_gen_init():
    temp_matrix = []
    dump_num = ran.randint(1, 9)
    for i in range(0, 9):
        while sudoku_array.__contains__(dump_num) and len(sudoku_array) < 9:
            dump_num = ran.randint(1, 9)
        sudoku_array.append(dump_num)

    # shift left 3 to add first 3-row slice
    temp_matrix = np.vstack((sudoku_array, sudoku_array[3:] + sudoku_array[0:3], sudoku_array[6:] + sudoku_array[0:6]))

    # shif left 1, and 2 times 3-elem shift to add second 3-row slice
    temp = sudoku_array[6:] + sudoku_array[0:6]
    temp = temp[1:] + [temp[0]]
    temp_matrix = np.vstack((temp_matrix, temp, temp[3:] + temp[0:3], temp[6:] + temp[0:6]))

    # shif left 1, and 2 times 3-elem shift to add third 3-row slice
    temp = temp[6:] + temp[0:6]
    temp = temp[1:] + [temp[0]]
    temp_matrix = np.vstack((temp_matrix, temp, temp[3:] + temp[0:3], temp[6:] + temp[0:6]))

    return temp_matrix # generated sudoku field


# sudoku dict key:0-9, values: rows
def sudoku_gen_getmap(sudoku_field):
    sudoku_row_map = {}
    try:
        assert np.shape(sudoku_field) == (9, 9)
    except AssertionError:
        raise Exception('Input Sudoku is not of 9 by 9 in size')
        return 0

    for i in range(0, 9):
        sudoku_row_map[i] = sudoku_field[i, :]
    return sudoku_row_map


# print generated sudoku
def sudoku_gen_print(sudoku_field):
    try:
        assert np.shape(sudoku_field) == (9, 9)
    except AssertionError:
        raise Exception('Input Sudoku is not of 9 by 9 in size')
        return 0
    print("\n".join([str(sudoku_gen_getmap(sudoku_field)[i]) for i in sudoku_gen_getmap(sudoku_field)]))
    return 1


