import numpy as np
from train_resource import sudoku_gen as sgen


def sudoku_batch100_gen_init(concat_sudoku):
    concat_sudoku = np.reshape(concat_sudoku, (9, 9, 1))
    try:
        assert np.shape(concat_sudoku) == (9, 9, 1)
    except AssertionError:
        raise Exception('Argument should at least contain one sudoku field! Create dummy variable to have one sudoku field')
        return 0

    for i in range(0, 9):
        temp_sudoku = sgen.sudoku_gen_init()
        temp_sudoku = np.reshape(temp_sudoku, (9, 9, 1))
        concat_sudoku = np.concatenate((concat_sudoku, temp_sudoku), axis=2)



    return concat_sudoku
