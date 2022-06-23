from rest_framework.serializers import ModelSerializer

from ..models import Article, NewsSetting


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class NewsSettingSerializer(ModelSerializer):
    class Meta:
        model = NewsSetting
        fields = '__all__'

