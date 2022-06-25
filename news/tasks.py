from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from config import celery_app
from news.utils import get_top_headlines, send_newsletter

from news.models import NewsSetting, Article


@celery_app.task
def curate_news():
    """
    Task which curates news periodically. - 15minutes
    """
    users = get_user_model().objects.filter(is_active=True)
    for user in users:
        # Check if setting object available for the user
        # if not go to next user
        try:
            news_setting = NewsSetting.objects.get(user=user)
        except NewsSetting.DoesNotExist:
            news_setting = None

        if news_setting is not None:
            titles = list(Article.objects.filter(owner=user).values_list('title', flat=True))
            country = news_setting.country
            sources = news_setting.sources
            top_headlines = get_top_headlines(country, sources)

            if top_headlines is not None:
                for top_headline in top_headlines:
                    if top_headline['title'] not in titles:
                        new_article = Article.objects.create(
                            owner=user,
                            title=top_headline['title'],
                            thumbnail=top_headline['urlToImage'],
                            url=top_headline['url'],
                            sources=top_headline['source']['name'],
                            country=country,
                        )
                        new_article.save()


@celery_app.task
def send_newsletter_task():
    """
    Task which sends newsletter to the user. - every hour
    * get all articles by last hour - if available
    * send newsletter to the user based on the keywords on users settings
    """
    users = get_user_model().objects.filter(is_active=True)
    for user in users:
        # Check if setting object available for the user
        # if not go to next user
        try:
            news_setting = NewsSetting.objects.get(user=user)
        except NewsSetting.DoesNotExist:
            news_setting = None

        if news_setting is not None:
            keywords = news_setting.keywords.split(',')
            articles = Article.objects.filter(owner=user)
            articles_last_hour = articles.filter(created_at__gt=datetime.now() - timedelta(hours=1))
            if articles_last_hour.exists():
                for article in articles_last_hour:
                    for keyword in keywords:
                        if keyword.casefold() in [word.casefold() for word in article.title.split()]:
                            send_newsletter(user, article.title, article.url)
                            break
