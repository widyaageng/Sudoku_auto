from test_resources import sudoku_test10_gen as stest10
from train_resource import sudoku_gen as sgen

# print(fetch.get_html_txt_headless('https://github.com/widyaageng/Sudoku_auto'))

dummy = sgen.sudoku_gen_init()
test10 = stest10.sudoku_test10_gen_init(dummy)
print(test10.shape)
print(test10[:, :, 0])
print(test10[:, :, 1])
