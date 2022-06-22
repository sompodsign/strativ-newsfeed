from django.db import models
from django.contrib.auth import get_user_model

from uuid import uuid4


User = get_user_model()


class UUIDMixin(models.Model):
    """
    A model mixin that adds a UUID field to a model.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(UUIDMixin):
    """
    A model representing a news article.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    thumbnail = models.URLField(max_length=200)
    url = models.URLField(max_length=200)
    sources = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# settings model
class Settings(UUIDMixin):
    """
    A model that stores the settings of the news for user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255, default='', blank=True)
    sources = models.CharField(max_length=500, default='', blank=True)
    keywords = models.TextField()
