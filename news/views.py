from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.contrib import messages

from .forms import SettingsForm
from .models import NewsSetting, Article


class NewsFeedView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'news_feed/feed.html'
    context_object_name = 'articles'
    paginate_by = 12

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        articles = Article.objects.filter(owner=user)
        return articles


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
        sources = news_setting.sources.split(',') if news_setting else []

        if news_setting:
            form = SettingsForm()
            form.fields['country'].initial = news_setting.country
            form.fields['sources'].initial = news_setting.sources.split(',')
            form.fields['keywords'].initial = news_setting.keywords
        return render(request, self.template, context={'form': form, 'sources': sources})

    def post(self, request):
        form = SettingsForm(request.POST)
        user = request.user
        news_setting = NewsSetting.objects.filter(user=user).first()
        query_data = dict(form.data)  # convert from query dict to dict to get lists data

        if news_setting:
            news_setting.country = query_data.get('country')[0]
            news_setting.sources = ", ".join(query_data.get('sources'))
            news_setting.keywords = ", ".join(query_data.get('keywords'))
            news_setting.save()
            messages.success(request, 'Settings updated successfully!')
        else:
            news_setting = NewsSetting(
                user=user,
                country=query_data.get('country')[0],
                sources=", ".join(query_data.get('sources')),
                keywords=", ".join(query_data.get('keywords'))
            )
            news_setting.save()
            if news_setting:
                messages.success(request, 'Settings saved successfully!')
            else:
                messages.error(request, 'Settings could not be saved!')

        return render(request, self.template, context={'form': form, 'sources': query_data.get('sources')})
