from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from news.utils import get_top_headlines


@login_required()
def news_view(request):
    all_news = get_top_headlines("us", sources=['fox-news', 'cbs'])
    return render(request, 'news_feed/portal.html', {'all_news': all_news})
