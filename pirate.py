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

    if stock_1_info or stock_2_info or stock_3_info or stock_4_info or stock_5_info or stock_6_info or stock_7_info or \
            stock_8_info or stock_9_info or stock_10_info:
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
