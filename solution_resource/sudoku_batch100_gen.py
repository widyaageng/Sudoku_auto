import numpy as np
from solution_resource import sudoku_gen as sgen


def sudoku_batch100_gen_init(concat_sudoku):
    concat_sudoku = concat_sudoku[:, :, np.newaxis]
    try:
        assert np.shape(concat_sudoku) == (9, 9, 1)
        print(np.shape(concat_sudoku))
    except AssertionError:
        raise Exception('Argument should at least contain one sudoku field! Create dummy variable to have one sudoku field')
        return 0

    for i in range(0, 100):
        print(sgen.sudoku_gen_init()[:, :, np.newaxis])
        concat_sudoku = np.concatenate((concat_sudoku, sgen.sudoku_gen_init()[:, :, np.newaxis]), axis=2)
    return concat_sudoku


test = sgen.sudoku_gen_init()
print(np.shape(test))
print(test)
print(sudoku_batch100_gen_init(test))
