from django import forms
from .models import Movie
class MovieForm(forms.ModelForm) :
    GENRE_A = 'comedy'
    GENRE_B = 'horror'
    GENRE_C = 'romance'

    GENRE_CHOICES = [
        (GENRE_A,'코미디'),
        (GENRE_B,'공포'),
        (GENRE_C,'로맨스')
    ] 

    title = forms.CharField(
        widget=forms.TextInput(
            # attributes
            attrs = {'placeholder':' title',}))
    audience = forms.IntegerField(
        widget=forms.NumberInput(
            # attributes
            attrs = {'placeholder':' Audience',}))
    poster_url = forms.CharField(
        widget=forms.TextInput(
            # attributes
            attrs = {'placeholder':' poster_url',}))
    description = forms.CharField(
        widget=forms.TextInput(
            # attributes
            attrs = {'placeholder':' description',}))      
    
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.Select()
    )

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs = {
                'min':0,
                'max' :5,
                'step':0.5 
            }
        )
    )
    release_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.SelectDateWidget)
    class Meta :
        model = Movie 

        fields = '__all__'