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
    def stock_1(self):
        if os.getenv('stock_1'):
            stock = os.getenv('stock_1')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_1_min'))
            maxi = float(os.getenv('stock_1_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_2(self):
        if os.getenv('stock_2'):
            stock = os.getenv('stock_2')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_2_min'))
            maxi = float(os.getenv('stock_2_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_3(self):
        if os.getenv('stock_3'):
            stock = os.getenv('stock_3')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_3_min'))
            maxi = float(os.getenv('stock_3_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_4(self):
        if os.getenv('stock_4'):
            stock = os.getenv('stock_4')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_4_min'))
            maxi = float(os.getenv('stock_4_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_5(self):
        if os.getenv('stock_5'):
            stock = os.getenv('stock_5')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_5_min'))
            maxi = float(os.getenv('stock_5_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_6(self):
        if os.getenv('stock_6'):
            stock = os.getenv('stock_6')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_6_min'))
            maxi = float(os.getenv('stock_6_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_7(self):
        if os.getenv('stock_7'):
            stock = os.getenv('stock_7')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_7_min'))
            maxi = float(os.getenv('stock_7_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_8(self):
        if os.getenv('stock_8'):
            stock = os.getenv('stock_8')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_8_min'))
            maxi = float(os.getenv('stock_8_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_9(self):
        if os.getenv('stock_9'):
            stock = os.getenv('stock_9')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_9_min'))
            maxi = float(os.getenv('stock_9_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None

    def stock_10(self):
        if os.getenv('stock_10'):
            stock = os.getenv('stock_10')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_10_min'))
            maxi = float(os.getenv('stock_10_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
                         '85%) smartphone_Mend(0px)'})[0].text.split(' - ')[1].split(',')[0]

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
        else:
            return None
