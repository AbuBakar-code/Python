import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "G4RHOWJK5UYIQNPC"
NEWS_API_KEY = "466f7426cbd748f28175291a6d564f6b"
TWILIO_SID = "ACa6256cb4edef6d944482e794182e716d"
TWILIO_AUTH_TOKEN = "33d5a510a21132a416598124781ceb9e"


stock_params = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": STOCK_API_KEY,
}

# Yesterday's stock closing price
response = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]

# Day before yesterday's stock closing price
day_before_yesterday = data_list[1]
day_before_yesterday_closing_data = day_before_yesterday["4. close"]
# Calculate positive difference b/w closing prices
difference = abs(float(yesterday_closing_data) - float(day_before_yesterday_closing_data))

# Calculate percentage b/w closing price 
diff_percent = (difference / float(yesterday_closing_data)) * 100

if diff_percent > 5:
  news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
  }
  news_response = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = news_response.json()['articles']

  three_articles = articles[:3]

  formatted_articles = [f"Headlines: {article['title']}.\n Brief: {article['description']}" for article in three_articles]

  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  for article in formatted_articles:
    message = client.messages.create(
      body= article,
      from_="+19377708173",
      to= "+923065312175"
    )
  
#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

