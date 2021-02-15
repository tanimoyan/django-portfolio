from django import forms
from .models import Image, Post

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'title']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'topimage', 'image', 'skill', 'github']