from django import forms
from .models import (
    Press, Teaching, About, Work
)
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget

class PressForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'Enter date of press',
        'id': 'date_picker',
    }))
    feature = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Feature title in caps eg "PRINT"'
    }))
    
    
    class Meta:
        model = Press
        exclude = ['created',]
        
        labels = {
            'reference': '',
            'feature': '',
        }
        
        widgets = {
            'reference': forms.Textarea(attrs={
                'placeholder': 'Reference in a few words',
                'rows': 10,
                'cols': 30,
            }),
            'link': forms.URLInput(attrs={
                'placeholder': 'Link to press',
              
            })
        }



class AboutForm(forms.ModelForm):
    
    content = RichTextFormField(widget=CKEditorWidget(), label='')
    
    
    class Meta:
        model = About
        exclude = ['created',]
        
        # labels = {
        #     'content': '',
            
        # }
        


class WorkForm(forms.ModelForm):
    
    content = RichTextFormField(widget=CKEditorWidget(), label='')
    
    
    class Meta:
        model = Work
        exclude = ['created',]
        
        
       


class TeachingForm(forms.ModelForm):
    
    content = RichTextFormField(widget=CKEditorWidget(), label='')
    
    
    class Meta:
        model = Teaching
        exclude = ['created',]
        
        
       
             