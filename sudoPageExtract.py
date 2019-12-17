from util import svg_dict
from web_fetch import fetch

# Retrieve plain HTML source
soup = fetch.get_html_txt_headless('https://sudoku.com/medium/')
fetch.close_html_txt_headless()

# Getting SVG list of initial numbers in the sudoku board
num_list = []
div_id_game_init = soup.find_all("path", attrs={"fill": "#344861", "fill-rule": "evenodd"})
div_id_game_user = soup.find_all("div", attrs={"class": "cell-value"})
for div_id in div_id_game_init:
    num_list.append(div_id['d'])

# Debug stuff
print('Total nums %d' % len(div_id_game_init))
number_retrieved = [svg_dict.get_svg_to_num(i) for i in num_list[-9:]]
cell_pre_exist_number = [svg_dict.get_svg_to_num(i) for i in num_list[0:-9]]
print(cell_pre_exist_number)
print(len(cell_pre_exist_number))
