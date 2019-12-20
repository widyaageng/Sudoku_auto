from web_fetch import fetch
from web_fetch import sudoku_extract
from train_resource import sudoku_gen as sgen
from train_resource import sudoku_batch100_gen as sgen100

# print(fetch.get_html_txt_headless('https://github.com/widyaageng/Sudoku_auto'))

train_data = sgen100.sudoku_batch100_gen_init(sgen.sudoku_gen_init())
print(train_data.shape)
print(train_data[:, :, 0])
print(train_data[:, :, 99])
