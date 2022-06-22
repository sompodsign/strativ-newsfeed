from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .forms import SettingsForm
from news.utils import get_top_headlines
from .models import Settings


@login_required()
def news_view(request):
    all_news = get_top_headlines("us", sources=['fox-news', 'cbs'])
    return render(request, 'news_feed/portal.html', {'all_news': all_news})


class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'news_feed/news_settings.html', context={'form': SettingsForm})

    def post(self, request):
        form = SettingsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            Settings.objects.create(user=user,
                                    country=cd['country'],
                                    sources=cd['sources'],
                                    keywords=cd['keywords'])

