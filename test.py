from train_resource import sudoku_gen, sudoku_batch100_gen
from test_resources import sudoku_test10_gen, sudoku_test10_drop_number


# Getting 100 batch of train data
train_data = sudoku_gen.sudoku_gen_init()
sudoku_gen.sudoku_gen_print(train_data)
print(train_data.shape)
train_data = sudoku_batch100_gen.sudoku_batch100_gen_init(train_data)
print(train_data)
print(train_data.shape)

# Getting 10 batch of test data
test_data = sudoku_gen.sudoku_gen_init()
sudoku_gen.sudoku_gen_print(test_data)
print(test_data.shape)
test_data = sudoku_test10_gen.sudoku_test10_gen_init(test_data)
print(test_data)
print(test_data.shape)
test_data = sudoku_test10_drop_number.sudoku_drop_cell(test_data, )

