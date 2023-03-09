from .models import Text, Word
from django.forms import ModelForm, Textarea, TextInput


class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = ["body"]
        widgets = {
            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter text'
            }),
        }


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ["body"]
        widgets = {
            "body": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter word'
            }),
        }