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


class StockChecker:
    def stock_1(self):
        if os.getenv('stock_1') and os.getenv('stock_1_max') and os.getenv('stock_1_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_2(self):
        if os.getenv('stock_2') and os.getenv('stock_2_max') and os.getenv('stock_2_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_3(self):
        if os.getenv('stock_3') and os.getenv('stock_3_max') and os.getenv('stock_3_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_4(self):
        if os.getenv('stock_4') and os.getenv('stock_4_max') and os.getenv('stock_4_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_5(self):
        if os.getenv('stock_5') and os.getenv('stock_5_max') and os.getenv('stock_5_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_6(self):
        if os.getenv('stock_6') and os.getenv('stock_6_max') and os.getenv('stock_6_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_7(self):
        if os.getenv('stock_7') and os.getenv('stock_7_max') and os.getenv('stock_7_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_8(self):
        if os.getenv('stock_8') and os.getenv('stock_8_max') and os.getenv('stock_8_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_9(self):
        if os.getenv('stock_9') and os.getenv('stock_9_max') and os.getenv('stock_9_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_10(self):
        if os.getenv('stock_10') and os.getenv('stock_10_max') and os.getenv('stock_10_min'):
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_11(self):
        if os.getenv('stock_11') and os.getenv('stock_11_max') and os.getenv('stock_11_min'):
            stock = os.getenv('stock_11')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_11_min'))
            maxi = float(os.getenv('stock_11_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_12(self):
        if os.getenv('stock_12') and os.getenv('stock_12_max') and os.getenv('stock_12_min'):
            stock = os.getenv('stock_12')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_12_min'))
            maxi = float(os.getenv('stock_12_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_13(self):
        if os.getenv('stock_13') and os.getenv('stock_13_max') and os.getenv('stock_13_min'):
            stock = os.getenv('stock_13')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_13_min'))
            maxi = float(os.getenv('stock_13_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_14(self):
        if os.getenv('stock_14') and os.getenv('stock_14_max') and os.getenv('stock_14_min'):
            stock = os.getenv('stock_14')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_14_min'))
            maxi = float(os.getenv('stock_14_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_15(self):
        if os.getenv('stock_15') and os.getenv('stock_15_max') and os.getenv('stock_15_min'):
            stock = os.getenv('stock_15')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_15_min'))
            maxi = float(os.getenv('stock_15_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_16(self):
        if os.getenv('stock_16') and os.getenv('stock_16_max') and os.getenv('stock_16_min'):
            stock = os.getenv('stock_16')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_16_min'))
            maxi = float(os.getenv('stock_16_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_17(self):
        if os.getenv('stock_17') and os.getenv('stock_17_max') and os.getenv('stock_17_min'):
            stock = os.getenv('stock_17')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_17_min'))
            maxi = float(os.getenv('stock_17_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_18(self):
        if os.getenv('stock_18') and os.getenv('stock_18_max') and os.getenv('stock_18_min'):
            stock = os.getenv('stock_18')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_18_min'))
            maxi = float(os.getenv('stock_18_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_19(self):
        if os.getenv('stock_19') and os.getenv('stock_19_max') and os.getenv('stock_19_min'):
            stock = os.getenv('stock_19')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_19_min'))
            maxi = float(os.getenv('stock_19_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_20(self):
        if os.getenv('stock_20') and os.getenv('stock_20_max') and os.getenv('stock_20_min'):
            stock = os.getenv('stock_20')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_20_min'))
            maxi = float(os.getenv('stock_20_max'))
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_21(self):
        if os.getenv('stock_21') and os.getenv('stock_21_max') and os.getenv('stock_21_min'):
            stock = os.getenv('stock_21')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_21_min'))
            maxi = float(os.getenv('stock_21_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(21px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_22(self):
        if os.getenv('stock_22') and os.getenv('stock_22_max') and os.getenv('stock_22_min'):
            stock = os.getenv('stock_22')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_22_min'))
            maxi = float(os.getenv('stock_22_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(22px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_23(self):
        if os.getenv('stock_23') and os.getenv('stock_23_max') and os.getenv('stock_23_min'):
            stock = os.getenv('stock_23')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_23_min'))
            maxi = float(os.getenv('stock_23_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(23px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_24(self):
        if os.getenv('stock_24') and os.getenv('stock_24_max') and os.getenv('stock_24_min'):
            stock = os.getenv('stock_24')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_24_min'))
            maxi = float(os.getenv('stock_24_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(24px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_

    def stock_25(self):
        if os.getenv('stock_25') and os.getenv('stock_25_max') and os.getenv('stock_25_min'):
            stock = os.getenv('stock_25')
            global result
            r = requests.get(f'https://finance.yahoo.com/quote/{stock}')
            scrapped = bs(r.text, "html.parser")
            raw_data = scrapped.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0]
            price = float(raw_data.find('span').text)
            price_change = re.findall(r"\d+\.\d+", str(raw_data))
            threshold = float(os.getenv('stock_25_min'))
            maxi = float(os.getenv('stock_25_max'))
            stock_name = scrapped.find_all('div', {
                'class': 'D(ib) Mt(-5px) Mend(25px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw('
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
                print(f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n')
                message = f'{stock_name} is currently less than ${threshold}.\n\n{msg}\n'
                return message
            elif price > maxi:
                message_ = f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n'
                print(f'{stock_name} is currently more than ${maxi}.\n\n{msg}\n')
                return message_
