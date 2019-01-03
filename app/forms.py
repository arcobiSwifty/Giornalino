from django import forms
from .models import Article, Edition, Theme



class CreaArticolo(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'argument', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Inserisci il titolo...'}),
            'text': forms.Textarea(attrs={'rows': '15', 'class': 'form-control', 'placeholder': 'Inserisci il contenuto del tuo articolo...'})
        }
        labels = {
            'argument': 'tema',
            'text': 'contenuto'
        }
