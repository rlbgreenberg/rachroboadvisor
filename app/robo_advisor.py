# this is the "app/robo_advisor.py" file

import os
from dotenv import load_dotenv
import requests
load_dotenv() # go get env vars from the .env file
# adds the env vars to the surrounding environment 
# ... where can access them with the os module
# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
print(ALPHAVANTAGE_API_KEY)
exit()


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



symbol = "MSFT"
request_url = 

response = requests.get(reques_url)
print(type(response))
print(response.text)