from django import forms
from markdownx.fields import MarkdownxFormField

from blog.models import BlogPost


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'content']
