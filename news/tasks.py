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
            keywords = news_setting.keywords.split(',')
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
                        # send email to the user if keywords are found in new article
                        for keyword in keywords:
                            if keyword.lower() in (word.lower() for word in top_headline['title'].split(" ")):
                                send_newsletter(user, new_article.title, new_article.url)
                                break
