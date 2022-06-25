import environ
from django.conf import settings
from django.core.mail import send_mail
from newsapi import NewsApiClient


env = environ.Env()
news_api_key = env('NEWS_API_KEY')

# Init
newsapi = NewsApiClient(api_key=news_api_key)


def get_top_headlines(country, sources):
    """
    country: country code (e.g. 'us', 'gb', 'au')
    sources: sources list in string (e.g. 'abc-news,the-verge')
    * Get top headlines from newsapi.org by country
    * filter by sources
    """
    top_headlines_by_country = newsapi.get_top_headlines(country=country)
    articles = top_headlines_by_country.get('articles')
    top_headlines_by_sources = []

    for article in articles:
        article_id = article.get('source').get('id')
        if article_id is not None and article_id in sources:
            top_headlines_by_sources.append(article)
    return top_headlines_by_sources if top_headlines_by_sources else None


def get_sources(country):
    """
    based on country codes get sources from newsapi.org
    """
    sources_obj = newsapi.get_sources(country=country)
    sources = []
    for source in sources_obj.get('sources'):
        sources.append((source.get('id'), source.get('name')))
    return sources


def send_newsletter(user, title, url):
    """
    Task which sends newsletter to the user.
    """
    send_mail("New article match with keyword", f"{title} - {url}", settings.DEFAULT_FROM_EMAIL, [user.email])

