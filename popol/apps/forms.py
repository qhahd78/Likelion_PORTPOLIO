from django import forms
from .models import comment


class CommentForm(forms.ModelForm):

    class Meta: 
        model = Comment 
        fields = ('content',)
