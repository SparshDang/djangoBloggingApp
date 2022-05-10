from django import forms

from blogapp.models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text']
