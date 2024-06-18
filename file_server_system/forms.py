from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    description = forms.CharField(
       widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Describe the file?'}
        ),
        max_length=300,
        help_text='The max length of the text is 300.'
    )
    
    file = forms.FileField(help_text="Upload a file.")

    class Meta:
        model = Document
        fields = ['title', 'description', 'file']