from util import svg_dict
from web_fetch import fetch
import numpy as np


def get_field():
    # Create board matrix
    sudoku_field = []

    # Retrieve plain HTML source
    soup = fetch.get_html_txt_headless('https://sudoku.com/medium/')
    fetch.close_html_txt_headless()

    # Getting row list
    tr_row_elem = soup.find_all("div", attrs={"class": "cell-value"})
    for elem in tr_row_elem:
        if elem.contents[0] == "\xa0":
            # print("X")
            sudoku_field.append(0)
        else:
            # print(svg_dict.get_svg_to_num(elem.svg.path["d"]))
            sudoku_field.append(svg_dict.get_svg_to_num(elem.svg.path["d"]))

    sudoku_field = np.reshape(sudoku_field, (9, 9))
    return sudoku_field

