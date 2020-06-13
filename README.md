# Black Pearl
An application that alerts you via email and/or whatsapp when the stocks prices on your watchlist has either deceeded the MIN threshold or exceeded the MAX limit value.

Note: This is a tweaked version of the [stock_monitor](https://github.com/thevickypedia/yahoo_finance_monitor) application.

## Setup

1. git clone this repository and alter the code to use local env instead of aws client (refer previous commits to look at the changes made)

2. Run this command in your terminal to install necessary packages<br/>cd stock_monitor/lib && pip3 install -r requirements.txt

2. Make sure you add the following env variables (AWS: key value pairs in your ssm parameter store)
* ACCESS_KEY - AWS access key id
* SECRET_KEY - AWS secret access key
* SENDER - sender email address (verified via AWS SES)
* RECIPIENT - receiver email address (verified via AWS SES)
* ACCESS_KEY - AWS access to authenticate into your AWS account
* SECRET_KEY - AWS secret key
* stock_1 - Symbol for the stock you'd like to track (Eg: MSFT for Microsoft)
* stock_1_min - The minimum value below which you'd like to be notified
* stock_1_max - The maximum value above which you'd like to be notified
* Note: Keep increasing the # as you want more stocks to be tracked. (Limit: 25)
<br/><br/>Optional (If you'd like to setup whats app notifications else skip these):
* SID - S-ID from twilio
* TOKEN - Token from twilio
* SEND - sender whats app number (fromat - +1xxxxxxxxxx)
* RECEIVE - receiver whats app number (fromat - +1xxxxxxxxxx)<br><br>

## Usage

* Check the AWS lambda setup [here](https://github.com/thevickypedia/stock_hawk/blob/master/README.md#setup)
* To run local replace the AWSClients().* part to local env variables (os.getenv()) in [pirate.py](https://github.com/thevickypedia/black_pearl/blob/master/pirate.py#L138-L139) and [emailer.py](https://github.com/thevickypedia/black_pearl/blob/master/lib/emailer.py#L9-L10)
<br><br>
<Option 1:
  * Download an IDE such as [pycharm](https://www.jetbrains.com/pycharm/download/download-thanks.html).
  * Setup python3 interpreter
  * Add environment variables in configurations>
  
<Option 2:
  * Create a .sh file with the above environment variables and run it or manually set each environment variable
  * Run the command<br/><python3 stock_monitor/stock_monitor.py>
  
<Option 3:
  * Install a docker and set the entry point to stock_monitor.py>

Click [here](https://www.twilio.com/docs/whatsapp/quickstart/python) to get started with Twilio or refer [twilio](https://pypi.org/project/twilio/) docs for quick start.<br/>
If you prefer not to use whats app notifications then simply change send_whatsapp() to send_email() in [stock_monitor.py](https://github.com/thevickypedia/stock_monitor/blob/master/stock_monitor.py#L92) and add arguments 'data, context'<br/>
By doing this the [send_whatsapp()](https://github.com/thevickypedia/black_pearl/blob/master/pirate.py#L99) function will never be called.
