#! /usr/bin/env python3
"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   05.17.2020
 *
 **/"""

import os
from datetime import datetime, timedelta

from twilio.rest import Client

from lib.emailer import Emailer
from lib.watcher import StockChecker


def email_formatter():
    HLX_info = StockChecker().hlx()
    EXPE_info = StockChecker().expe()
    CCL_info = StockChecker().ccl()
    WORK_info = StockChecker().work()
    H_info = StockChecker().h()
    XOM_info = StockChecker().xom()

    if HLX_info or EXPE_info or CCL_info or WORK_info or H_info:
        email_text = 'Watchlist Notification\n'

        if HLX_info:
            email_text += '\nHelix Energy Report:\n'
            email_text += HLX_info

        if EXPE_info:
            email_text += '\nExpedia Report:\n'
            email_text += EXPE_info

        if CCL_info:
            email_text += '\nCarnival Report:\n'
            email_text += CCL_info

        if WORK_info:
            email_text += '\nSlack Report:\n'
            email_text += WORK_info

        if H_info:
            email_text += '\nHyatt Report:\n'
            email_text += H_info

        if XOM_info:
            email_text += '\nExxon Report:\n'
            email_text += H_info

        return email_text
    else:
        print('Nothing to notify, bye..')
        return None


def send_email():
    if email_formatter():
        sender_env = os.getenv('SENDER')
        recipient_env = os.getenv('RECIPIENT')
        git = 'https://github.com/vignesh1793/black_pearl'
        footer_text = "\n----------------------------------------------------------------" \
                      "----------------------------------------\n" \
                      "A report on the list shares on your watchlist that has either deceeded the MIN threshold or " \
                      "exceeded the MAX limit value.\n" \
                      "The data is being collected from https://finance.yahoo.com," \
                      f"\nFor more information check README.md in {git}"
        sender = f'Stock Hawk <{sender_env}>'
        recipient = [f'{recipient_env}']
        title = 'Stock Monitor Alert'
        text = f'{email_formatter()}\n\nNavigate to check logs: \n\n{footer_text}'
        email = Emailer(sender, recipient, title, text)
        return email
    else:
        return None


# two arguments for the below functions as lambda passes event, context by default
def send_whatsapp(data, context):
    if send_email():
        now = datetime.now() - timedelta(hours=5)
        dt_string = now.strftime("%A, %B %d, %Y %I:%M %p")
        sid = os.getenv('SID')
        token = os.getenv('TOKEN')
        sender = f"whatsapp:{os.getenv('SEND')}"
        receiver = f"whatsapp:{os.getenv('RECEIVE')}"
        client = Client(sid, token)
        from_number = sender
        to_number = receiver
        client.messages.create(body=f'{dt_string}\n\nBlack Pearl Notification\nLog info here\n',
                               from_=from_number,
                               to=to_number)
    else:
        return None


if __name__ == '__main__':
    send_whatsapp("data", "context")
