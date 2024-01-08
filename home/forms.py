from django import forms
from django.forms.models import inlineformset_factory
from .models import (
    Post, Comment, PostImage, PostVideo,
)
from embed_video.fields import EmbedVideoFormField


class PostForm(forms.ModelForm):
    video = EmbedVideoFormField(widget=forms.URLInput(attrs={
        'class': 'video'
    }))
  

    class Meta:
        model = Post
        exclude = ['author', 'created', 'videos', 'images']


class PostImageForm(forms.ModelForm):

    class Meta:
        model = PostImage
        exclude = ['post', 'created']


class PostVideoForm(forms.ModelForm):
    video = EmbedVideoFormField(widget=forms.URLInput(attrs={
        'placeholder': 'Insert video link'
    }))
    
    class Meta:
        model = PostVideo
        exclude = ['post', 'created']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ['post', 'author', 'created']
        labels = {
            'message':'',
         
        }
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'rows': 10,
                'cols': 30,
            })
        }
