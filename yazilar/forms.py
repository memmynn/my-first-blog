from django import forms

from .models import Yazi

class PostForm(forms.ModelForm):

    class Meta:
        model = Yazi
        fields = ('title', 'text',)