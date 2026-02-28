from django import forms

from store.models import ReviewRating 


class ReviewFom(forms.ModelForm):
    class Meta:
        model = ReviewRating   
        fields = ['subject','review','rating']
        