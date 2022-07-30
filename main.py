import requests


def get_news(topic, from_date, to_date, language = 'en', api_key = '1ecbb1e609744b0caf6bd0cbbf3e6da8'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    contents = r.json()
    articles = contents['articles']
    results = []

    for article in articles:
        results.append(f"TITLE\n'{article['title']},'\nDESCRIPTION\n', {article['description']}")
        
    return results

print(get_news(topic='space', from_date='2022-7-3', to_date='2022-7-4'))


    



