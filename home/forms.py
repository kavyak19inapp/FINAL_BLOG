from django import forms
<<<<<<< HEAD
from home.models import Post,Comment
=======
from home.models import Post
>>>>>>> f29d42077afee9e754d715fe753796273cca2451

class HomeForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('text','title',)
<<<<<<< HEAD
        
class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('text','author',)
=======
>>>>>>> f29d42077afee9e754d715fe753796273cca2451
