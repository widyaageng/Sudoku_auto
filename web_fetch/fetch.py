from selenium import webdriver
from bs4 import BeautifulSoup as bsoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

# start chrome browser
def get_html_txt_headless(web_address):
    try:
        assert type(web_address) == str
    except AssertionError as error:
        raise Exception('Input is not an address in string type!')
        return -1
    browser.get(web_address)
    html_cont = str(browser.page_source)
    soup = bsoup(html_cont, features='html.parser')
    return soup

def close_html_txt_headless():
    browser.close()
