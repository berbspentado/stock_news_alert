STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


import requests

API_KEY = '4VYS6M4ZU4ADGDGJ'
PARAMETERS = {
    'function':'TIME_SERIES_DAILY',
    'symbol':'TSLA',
    'interval':'5min',
    'apikey':API_KEY,

}
STOCK_URL = 'https://www.alphavantage.co/query?'


response = requests.get(STOCK_URL,params=PARAMETERS)
response.raise_for_status()
stock_data = response.json()

yesterday_date_index = list(stock_data["Time Series (Daily)"])[0]
previous_date_index = list(stock_data["Time Series (Daily)"])[1]

yesterday_price_closed = float(stock_data["Time Series (Daily)"][yesterday_date_index]['4. close'])
previousday_price_closed = float(stock_data["Time Series (Daily)"][previous_date_index]['4. close'])

difference = yesterday_price_closed - previousday_price_closed
average = (yesterday_price_closed + previousday_price_closed) / 2
percentage = (difference/average) * 100

if percentage > 5:
    print("Get News")
else:
    print("hatdog")
