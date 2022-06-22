from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .forms import SettingsForm
from news.utils import get_top_headlines
from .models import NewsSetting


@login_required()
def news_view(request):
    all_news = get_top_headlines("us", sources=['fox-news', 'cbs'])
    return render(request, 'news_feed/portal.html', {'all_news': all_news})


class SettingsView(LoginRequiredMixin, View):
    """
    This is the view which handles the settings of the news feed.
    * The user can change the settings of the news feed.
    * The user can update or create a new settings.
    """

    template = 'news_feed/news_settings.html'

    def get(self, request):
        user = request.user
        form = SettingsForm()
        news_setting = NewsSetting.objects.filter(user=user).first()
        if news_setting:
            form = SettingsForm()
            form.fields['country'].initial = news_setting.country
            form.fields['sources'].initial = news_setting.sources.split(',')
            form.fields['keywords'].initial = news_setting.keywords
        return render(request, self.template, context={'form': form})

    def post(self, request):
        form = SettingsForm(request.POST)
        user = request.user
        news_setting = NewsSetting.objects.filter(user=user).first()
        if form.is_valid():
            if news_setting:
                news_setting.country = form.cleaned_data['country']
                news_setting.sources = ','.join(form.cleaned_data['sources'])
                news_setting.keywords = form.cleaned_data['keywords']
                news_setting.save()
            else:
                news_setting = NewsSetting(
                    user=user,
                    country=form.cleaned_data['country'],
                    sources=','.join(form.cleaned_data['sources']),
                    keywords=form.cleaned_data['keywords']
                )
                news_setting.save()
        return render(request, self.template, context={'form': form})
