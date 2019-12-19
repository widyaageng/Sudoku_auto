import numpy as np
from solution_resource import sudoku_gen as sgen


def sudoku_batch100_gen_init(concat_sudoku):
    try:
        assert np.shape(concat_sudoku) == (9, 9)
    except AssertionError:
        raise Exception('Argument should at least contain one sudoku field!')
        return 0

    for i in range(0, 100):
        concat_sudoku = np.concatenate(concat_sudoku, axis=-1)
    return concat_sudoku


print(sudoku_batch100_gen_init(sgen))
