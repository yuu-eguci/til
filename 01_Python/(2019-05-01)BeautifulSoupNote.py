
"""BeautifulSoupNote

pipenv install beautifulsoup4 lxml

"""


from bs4 import BeautifulSoup


# requests.text 等で取得した文字列とする。
text = ''

# これでパース。
soup = BeautifulSoup(text, 'lxml')

# セレクタ指定で取得。これは CSS に慣れているぼくにはわかりやすい。
ones = soup.select('#id-name')
one = soup.select_one('#id-name')

# 取得したタグから attribute を取得。これは JQuery に慣れているぼくにはわかりやすい。
attr = one['data-price']

# 取得したタグから中のテキストを取得。
text = one.get_text()
