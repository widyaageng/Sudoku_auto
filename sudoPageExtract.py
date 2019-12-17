from util import svg_dict
from web_fetch import fetch

# Retrieve plain HTML source
soup = fetch.get_html_txt_headless('https://sudoku.com/medium/')
fetch.close_html_txt_headless()

# print(soup.prettify())
num_list = []
div_id_game = soup.find_all("path", attrs={"fill": "#344861", "fill-rule": "evenodd" })
for div_id in div_id_game:
    num_list.append(div_id['d'])

print('Total nums %d' % len(div_id_game))
number_retrieved = [svg_dict.get_svg_to_num(i) for i in num_list[-9:]]
cell_pre_exist_number = [svg_dict.get_svg_to_num(i) for i in num_list[0:-9]]
print(cell_pre_exist_number)
print(len(cell_pre_exist_number))
