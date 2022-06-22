from django.contrib.auth import get_user_model
from news.utils import get_top_headlines

from config import celery_app

from news.models import NewsSetting, Article


@celery_app.task
def curate_news():
    """
    Task which curates news periodically. - 15minutes
    """
    users = get_user_model().objects.filter(is_active=True)
    for user in users:
        news_setting = NewsSetting.objects.get(user=user)
        articles = list(Article.objects.filter(owner=user).values_list('title', flat=True))

        if news_setting.is_active:
            country = news_setting.country
            sources = news_setting.sources
            top_headlines = get_top_headlines(country, sources)

            for top_headline in top_headlines:
                if top_headline['title'] not in articles:
                    Article.objects.create(
                        owner=user,
                        title=top_headline['title'],
                        thumbnail=top_headline['urlToImage'],
                        url=top_headline['url'],
                        sources=top_headline['source']['name'],
                        country=top_headline['source']['name']
                    )
