from util import sudokufy
from train_resource import sudoku_gen as sgen
from test_resources import sudoku_test10_drop_number as testdrop10
import random
from util import sudoku_flat

# print(fetch.get_html_txt_headless('https://github.com/widyaageng/Sudoku_auto'))

random.seed(0)
testfield = sgen.sudoku_gen_init()
print(testfield)
testfield = testdrop10.sudoku_drop_cell(testfield, 40)
print(testfield)
testfield = sudoku_flat.flat_sudoku_to_col_vec(testfield)
print(testfield)
print(testfield.shape)
testfield = sudoku_flat.flat_sudoku_to_row_vec(testfield)
print(testfield)
print(testfield.shape)
