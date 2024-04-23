from django import forms
from .models import Movie,User

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','description','release_date','poster','actors','category','trailer_link']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password']

