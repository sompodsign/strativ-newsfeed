from rest_framework.serializers import ModelSerializer

from ..models import Article, NewsSetting


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'thumbnail', 'url', 'sources', 'country', 'created_at', 'updated_at')


class NewsSettingSerializer(ModelSerializer):
    class Meta:
        model = NewsSetting
        fields = ('id', 'country', 'sources', 'keywords', 'created_at', 'updated_at')

