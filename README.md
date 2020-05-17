# Black Pearl
A report on the list shares on your watchlist that has either deceeded the MIN threshold or exceeded the MAX limit value.

## Setup

1. git clone this repository

2. Run this command in your terminal to install necessary packages<br/>cd stock_monitor/lib && pip3 install -r requirements.txt

2. Make sure you add the following env variables
* ACCESS_KEY - AWS access key id
* SECRET_KEY - AWS secret access key
* SENDER - sender email address (verified via AWS SES)
* RECIPIENT - receiver email address (verified via AWS SES)
* ACCESS_KEY - AWS access to authenticate into your AWS account
* SECRET_KEY - AWS secret key
* HLX_threshold, EXPE_threshold, CCL_threshold, WORK_threshold, H_threshold, XOM_threshold - Minimum value below which you'd like to be notified
* HLX_max, EXPE_max, CCL_max, WORK_max, H_max, XOM_max - Maximum value after which you'd like to be notified
<br/><br/>Optional (If you'd like to setup whats app notifications else skip these):
* SID - S-ID from twilio
* TOKEN - Token from twilio
* SEND - sender whats app number (fromat - +1xxxxxxxxxx)
* RECEIVE - receiver whats app number (fromat - +1xxxxxxxxxx)<br><br>

## Usage

Option 1:
  * Download an IDE such as [pycharm](https://www.jetbrains.com/pycharm/download/download-thanks.html).
  * Setup python3 interpreter
  * Add environment variables in configurations
  
Option 2:
  * Create a .sh file with the above environment variables and run it or manually set each environment variable
  * Run the command<br/>python3 stock_monitor/stock_monitor.py
  
Option 3:
  * Install a docker and set the entry point to stock_monitor.py

Click [here](https://www.twilio.com/docs/whatsapp/quickstart/python) to get started with Twilio or refer [twilio](https://pypi.org/project/twilio/) docs for quick start.<br/>
If you prefer not to use whats app notifications then simply change send_whatsapp() to send_email() in [stock_monitor.py](https://github.com/vignesh1793/stock_monitor/blob/master/stock_monitor.py#L92) and add arguments 'data, context'<br/>
By doing this the [send_whatsapp()](https://github.com/vignesh1793/black_pearl/blob/master/pirate.py#L99) function will never be called.
