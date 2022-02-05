from django import forms

from .models import BlogModel


class CreateBlog(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude = ('owner',)
