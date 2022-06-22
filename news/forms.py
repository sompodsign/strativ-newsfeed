from django import forms
from django.conf import settings


class SettingsForm(forms.Form):
    """
    Form for Settings model
    * country dropdown
    * sources checkbox
    * keywords textarea
    """
    country = forms.ChoiceField(
        choices=settings.COUNTRY_CHOICES,
        label='Country',
        widget=forms.Select(attrs={'class': 'form-control'}))

    sources = forms.MultipleChoiceField(
        choices=settings.SOURCE_CHOICES,
        label='Sources', )

    keywords = forms.CharField(
        label='Keywords',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Crime, Donald Trump, Google'}),
    )

