import numpy as np
from train_resource import sudoku_gen as sgen


# Generating 10 completed test sudoku matrices
def sudoku_test10_gen_init(concat_sudoku):
    concat_sudoku = concat_sudoku[:, :, np.newaxis]
    try:
        assert np.shape(concat_sudoku) == (9, 9, 1)
    except AssertionError:
        raise Exception('Argument should at least contain one sudoku field! Create dummy variable to have one sudoku field')
        return 0

    for i in range(0, 9):
        temp_sudoku = sgen.sudoku_gen_init()
        temp_sudoku = temp_sudoku[:, :, np.newaxis]
        concat_sudoku = np.dstack((concat_sudoku, temp_sudoku))
    return concat_sudoku

