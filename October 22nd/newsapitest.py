import os
from newsapi import NewsApiClient

api_key = os.environ["API_KEY"]
newsapi = NewsApiClient(api_key=api_key)

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

print(top_headlines)

