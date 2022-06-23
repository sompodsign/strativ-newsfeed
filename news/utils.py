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
    * Get top headlines from newsapi.org
    """

    # two different requests because country and sources can't be together according to newsapi.org
    top_headlines_by_country = newsapi.get_top_headlines(country=country)
    top_headlines_by_source = newsapi.get_top_headlines(sources=sources)

    # combining the two responses
    top_headlines = top_headlines_by_country.get('articles') + top_headlines_by_source.get('articles')
    return top_headlines


def send_newsletter(user, title, url):
    """
    Task which sends newsletter to the user.
    """
    send_mail("New article match with keyword", f"{title} - {url}", settings.DEFAULT_FROM_EMAIL, [user.email])

