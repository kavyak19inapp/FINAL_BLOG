from django import forms
from home.models import Post,Comment

class HomeForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('text','title',)
        
class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('text','author',)
