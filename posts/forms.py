# Django
from django import forms

# Django
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('user','profile','title','photo')