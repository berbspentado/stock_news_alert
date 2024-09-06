from twilio.rest import Client
import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL = 'https://www.alphavantage.co/query?'
NEWS_URL = 'https://newsapi.org/v2/everything?'

API_KEY_STOCK = os.environ.get("API_KEY_STOCK")
API_KEY_NEWS = os.environ.get("API_KEY_NEWS")

TWILIO_TOKEN = os.environ.get("API_KEY_TWILIO")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")

PARAMETERS_STOCKS = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'interval':'5min',
    'apikey':API_KEY_STOCK,

}
stock_response = requests.get(STOCK_URL,params=PARAMETERS_STOCKS)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_date_index = list(stock_data["Time Series (Daily)"])[0]
previous_date_index = list(stock_data["Time Series (Daily)"])[1]

yesterday_price_closed = float(stock_data["Time Series (Daily)"][yesterday_date_index]['4. close'])
previousday_price_closed = float(stock_data["Time Series (Daily)"][previous_date_index]['4. close'])

difference = yesterday_price_closed - previousday_price_closed
average = (yesterday_price_closed + previousday_price_closed) / 2
percentage = (difference/average) * 100

if percentage > 5:
    print(percentage)
    print("Get News")

    PARAMETERS_NEWS ={
    'q': COMPANY_NAME,
    'apikey':API_KEY_NEWS,
    'from':'2024-09-03',
    'to':'2024-09-04',
}

    news_response = requests.get(NEWS_URL,params=PARAMETERS_NEWS)
    news_response.raise_for_status()
    news_data = news_response.json()
    three_articles = news_data['articles'][0:3]

    for article in three_articles:
        article_title = article['title']
        article_publisher = article['source']['name']
        print(f"{STOCK}: {percentage}\nHeadline: {article_title}" )

        client = Client(ACCOUNT_SID, TWILIO_TOKEN)
        message = client.messages.create(
        body=f"{STOCK}: {percentage}\nHeadline: {article_title}",
        from_="+12111111111", #DUMMY NUMBER
        to="+639111111111", #DUMMY NUMBER
    )
        print(message.status)






