#! /usr/bin/env python3
"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   05.17.2020
 *
 **/"""

import os
import re

import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

current_time = datetime.now()
utc_to_cdt = current_time - timedelta(hours=5)
dt_string = utc_to_cdt.strftime("%A, %B %d, %Y %I:%M %p")
print(f'Data as of {dt_string}\n')


class StockChecker:
    def hlx(self):
        stock = 'HLX'
        stock_name = 'Helix Energy'
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('HLX_threshold'))
        maxi = float(os.getenv('HLX_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        msg = f"The current price of {stock} is: ${price}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'{stock_name}:\n{msg}\n')
        elif price < threshold:
            message = f'Data as of {dt_string}:\n\n{stock_name} is currently less than ${threshold}.\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Data as of {dt_string}:\n\n{stock_name} is currently more than ${maxi}.\n{msg}\n'
            return message_

    def expe(self):
        stock = 'EXPE'
        stock_name = 'Expedia'
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('EXPE_threshold'))
        maxi = float(os.getenv('EXPE_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        msg = f"The current price of {stock} is: ${price}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'{stock_name}:\n{msg}\n')
        elif price < threshold:
            message = f'Data as of {dt_string}:\n\n{stock_name} is currently less than ${threshold}.\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Data as of {dt_string}:\n\n{stock_name} is currently more than ${maxi}.\n{msg}\n'
            return message_

    def ccl(self):
        stock = 'CCL'
        stock_name = 'Carnival'
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('CCL_threshold'))
        maxi = float(os.getenv('CCL_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        msg = f"The current price of {stock} is: ${price}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'{stock_name}:\n{msg}\n')
        elif price < threshold:
            message = f'Data as of {dt_string}:\n\n{stock_name} is currently less than ${threshold}.\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Data as of {dt_string}:\n\n{stock_name} is currently more than ${maxi}.\n{msg}\n'
            return message_

    def work(self):
        stock = 'WORK'
        stock_name = 'Slack Technologies'
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('WORK_threshold'))
        maxi = float(os.getenv('WORK_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        msg = f"The current price of {stock} is: ${price}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'{stock_name}:\n{msg}\n')
        elif price < threshold:
            message = f'Data as of {dt_string}:\n\n{stock_name} is currently less than ${threshold}.\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Data as of {dt_string}:\n\n{stock_name} is currently more than ${maxi}.\n{msg}\n'
            return message_

    def h(self):
        stock = 'H'
        stock_name = 'Hyatt Hotels'
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('H_threshold'))
        maxi = float(os.getenv('H_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        msg = f"The current price of {stock} is: ${price}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'{stock_name}:\n{msg}\n')
        elif price < threshold:
            message = f'Data as of {dt_string}:\n\n{stock_name} is currently less than ${threshold}.\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Data as of {dt_string}:\n\n{stock_name} is currently more than ${maxi}.\n{msg}\n'
            return message_

    def xom(self):
        stock = 'XOM'
        stock_name = 'Exxon Mobil'
        global result
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
        scrapped = bs(r.text, "html.parser")
        raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
        price = float(raw_data.find('span').text)
        price_change = re.findall(r"\d+\.\d+", str(raw_data))
        threshold = float(os.getenv('XOM_threshold'))
        maxi = float(os.getenv('XOM_max'))

        if 'At close' in str(raw_data):
            result = 'currently no change. Last change:'
        elif 'negativeColor' in str(raw_data):
            result = 'decreased'
        elif 'positiveColor' in str(raw_data):
            result = 'increased'
        msg = f"The current price of {stock} is: ${price}\n{stock} share has {result} ${price_change[-2]}"

        if result == 'currently no change. Last change:':
            print(f'{stock_name}:\n{msg}\n')
        elif price < threshold:
            message = f'Data as of {dt_string}:\n\n{stock_name} is currently less than ${threshold}.\n{msg}\n'
            return message
        elif price > maxi:
            message_ = f'Data as of {dt_string}:\n\n{stock_name} is currently more than ${maxi}.\n{msg}\n'
            return message_
