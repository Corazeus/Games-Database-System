from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import Game, Genre, Developer, Platform, Rating, Region, Sales


class RegisterGameForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    year_released = forms.CharField(widget=forms.NumberInput)
    # game_img = forms.CharField(widget=forms.TextInput)
    # nakaforeignkey
    genre_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Genre.objects.only('genre_name'))
    developer_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Developer.objects.only('developer_name'))
    platform_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Platform.objects.only('platform_name'))
    rating_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Rating.objects.only('evaluation'))

    class Meta:
        model = Game
        fields = ['name', 'genre_id', 'developer_id', 'platform_id', 'rating_id', 'year_released', 'game_img']

    def __init__(self, *args, **kwargs):
        super(RegisterGameForm, self).__init__(*args, *kwargs)


class AddPlatformForm(ModelForm):
    platform_id = forms.CharField(widget=forms.TextInput)
    platform_name = forms.CharField(widget=forms.TextInput)
    platform_developer = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Platform
        fields = ['platform_id', 'platform_name', 'platform_developer']

    def __init__(self, *args, **kwargs):
        super(AddPlatformForm, self).__init__(*args, **kwargs)


class AddDeveloperForm(ModelForm):
    developer_name = forms.CharField(widget=forms.TextInput)
    location = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Developer
        fields = ['developer_name', 'location']


class RegisterSalesForm(ModelForm):
    sales = forms.CharField(widget=forms.NumberInput)
    game_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Game.objects.only('name'))
    region_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Region.objects.only('region_name'))
    year = forms.CharField(widget=forms.NumberInput)

    class Meta:

        model = Sales
        fields = ['sales', 'game_id', 'region_id','year']


class EditGameForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    year_released = forms.CharField(widget=forms.NumberInput)
    # game_img = forms.CharField(widget=forms.TextInput)
    # nakaforeignkey
    genre_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Genre.objects.only('genre_name'))
    developer_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Developer.objects.only('developer_name'))
    platform_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Platform.objects.only('platform_name'))
    rating_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Rating.objects.only('evaluation'))

    class Meta:
        model = Game
        fields = ['name', 'genre_id', 'developer_id', 'platform_id', 'rating_id', 'year_released', 'game_img']


class EditPlatformForm(ModelForm):
    platform_developer = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Platform
        fields = ['platform_developer']