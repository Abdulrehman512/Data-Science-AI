from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='956e27ab1fbc4481be3f89432027a4ae')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='Elon Musk',
                                          category='business',
                                          language='en'
)

dt = top_headlines["articles"]

for x,y in enumerate(dt):
    print(f"{x} {y['description']}")