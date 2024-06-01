import RPi_I2C_driver
import time
import requests

mylcd = RPi_I2C_driver.lcd()
headers = {"accept": "application.json"}
url_btc = "https://api.bithumb.com/public/transaction_history/BTC_KRW"

def str_format(string, length):
    if "." in string:
        result = "{:,}".format(float(string))
    else:
        result = "{:,}".format(int(string))
    result = result + " KRW"
    for i in range(length - len(result)):
        result = result + " "
    return result

def print_price(token, count):
    url = "https://api.bithumb.com/public/transaction_history/" + token + "_KRW"
    mylcd.lcd_display_string(token + " Price", 1)
    for i in range(count):
        response = requests.get(url, headers = headers)
        idx1 = response.text.rfind("price") + 8
        idx2 = response.text.rfind("total") - 3
        string = str_format(response.text[idx1:idx2], 16)
        mylcd.lcd_display_string(string, 2)
        time.sleep(1)

while True:
    tokens = ["BTC", "ETH"]
    for tok in tokens:
        mylcd.lcd_display_string("                ", 1)
        print_price(tok, 3)
