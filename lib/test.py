import requests
from bs4 import BeautifulSoup as bs
import re
import os

stock = os.getenv('stock_1')
r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
scrapped = bs(r.text, "html.parser")
raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
price = float(raw_data.find('span').text)
price_change = re.findall(r"\d+\.\d+", str(raw_data))

# soup = bs(r.text, "lxml")
# title = soup.find("meta",  property="og:title")
# url = soup.find("meta",  property="og:url")
# print(title["content"] if title else "No meta title given")
raw_d = scrapped.find_all('div', {'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                                           '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

print(raw_d)
