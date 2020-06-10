#! /usr/bin/env python3
"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   05.17.2020
 *
 **/"""

import os

from twilio.rest import Client

from lib.emailer import Emailer
from lib.watcher import StockChecker
from datetime import datetime, timedelta

current_time = datetime.now()
utc_to_cdt = current_time - timedelta(hours=5)
dt_string = utc_to_cdt.strftime("%A, %B %d, %Y %I:%M %p")
print(f'Data as of {dt_string}\n')


def email_formatter():
    stock_1_info = StockChecker().stock_1()
    stock_2_info = StockChecker().stock_2()
    stock_3_info = StockChecker().stock_3()
    stock_4_info = StockChecker().stock_4()
    stock_5_info = StockChecker().stock_5()
    stock_6_info = StockChecker().stock_6()
    stock_7_info = StockChecker().stock_7()
    stock_8_info = StockChecker().stock_8()
    stock_9_info = StockChecker().stock_9()
    stock_10_info = StockChecker().stock_10()
    stock_11_info = StockChecker().stock_11()
    stock_12_info = StockChecker().stock_12()
    stock_13_info = StockChecker().stock_13()
    stock_14_info = StockChecker().stock_14()
    stock_15_info = StockChecker().stock_15()
    stock_16_info = StockChecker().stock_16()
    stock_17_info = StockChecker().stock_17()
    stock_18_info = StockChecker().stock_18()
    stock_19_info = StockChecker().stock_19()
    stock_20_info = StockChecker().stock_20()
    stock_21_info = StockChecker().stock_21()
    stock_22_info = StockChecker().stock_22()
    stock_23_info = StockChecker().stock_23()
    stock_24_info = StockChecker().stock_24()
    stock_25_info = StockChecker().stock_25()

    if stock_1_info or stock_2_info or stock_3_info or stock_4_info or stock_5_info or stock_6_info or stock_7_info or \
            stock_8_info or stock_9_info or stock_10_info or stock_11_info or stock_12_info or stock_13_info or \
            stock_14_info or stock_15_info or stock_16_info or stock_17_info or stock_18_info or stock_19_info or \
            stock_20_info or stock_21_info or stock_22_info or stock_23_info or stock_24_info or stock_25_info:
        email_text = f'Watchlist Notification\n\n'

        if stock_1_info:
            email_text += stock_1_info

        if stock_2_info:
            email_text += stock_2_info

        if stock_3_info:
            email_text += stock_3_info

        if stock_4_info:
            email_text += stock_4_info

        if stock_5_info:
            email_text += stock_5_info

        if stock_6_info:
            email_text += stock_6_info

        if stock_7_info:
            email_text += stock_7_info

        if stock_8_info:
            email_text += stock_8_info

        if stock_9_info:
            email_text += stock_9_info

        if stock_10_info:
            email_text += stock_10_info

        if stock_11_info:
            email_text += stock_11_info

        if stock_12_info:
            email_text += stock_12_info

        if stock_13_info:
            email_text += stock_13_info

        if stock_14_info:
            email_text += stock_14_info

        if stock_15_info:
            email_text += stock_15_info

        if stock_16_info:
            email_text += stock_16_info

        if stock_17_info:
            email_text += stock_17_info

        if stock_18_info:
            email_text += stock_18_info

        if stock_19_info:
            email_text += stock_19_info

        if stock_20_info:
            email_text += stock_20_info

        if stock_21_info:
            email_text += stock_21_info

        if stock_22_info:
            email_text += stock_22_info

        if stock_23_info:
            email_text += stock_23_info

        if stock_24_info:
            email_text += stock_24_info

        if stock_25_info:
            email_text += stock_25_info

        return email_text
    else:
        print('Nothing to notify, bye..')


def send_email():
    email_check = email_formatter()
    if email_check:
        sender_env = os.getenv('SENDER')
        recipient_env = os.getenv('RECIPIENT')
        git = 'https://github.com/thevickypedia/black_pearl'
        logs = 'https://us-west-2.console.aws.amazon.com/cloudwatch/home#logStream:group=/aws/lambda/black_pearl'
        footer_text = "\n----------------------------------------------------------------" \
                      "----------------------------------------\n" \
                      "A report on the list shares on your watchlist that has either deceeded the MIN threshold or " \
                      "exceeded the MAX limit value.\n" \
                      "The data is being collected from https://finance.yahoo.com," \
                      f"\nFor more information check README.md in {git}"
        sender = f'Black Pearl <{sender_env}>'
        recipient = [f'{recipient_env}']
        title = f'Black Pearl Alert as of {dt_string}'
        text = f'{email_check}\n\nNavigate to check logs: {logs}\n\n{footer_text}'
        Emailer(sender, recipient, title, text)
        return email_check


# two arguments for the below functions as lambda passes event, context by default
def send_whatsapp(data, context):
    checker = send_email()
    if checker:
        sid = os.getenv('SID')
        token = os.getenv('TOKEN')
        sender = f"whatsapp:{os.getenv('SEND')}"
        receiver = f"whatsapp:{os.getenv('RECEIVE')}"
        client = Client(sid, token)
        from_number = sender
        to_number = receiver
        client.messages.create(body=checker,
                               from_=from_number,
                               to=to_number)


if __name__ == '__main__':
    send_whatsapp("data", "context")
