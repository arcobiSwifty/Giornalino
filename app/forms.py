from django import forms
from .models import Article, Edition, Theme



class CreaArticolo(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'author', 'argument', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Inserisci il titolo'}),
            'text': forms.Textarea(attrs={'rows': '10', 'class': 'form-control', 'placeholder': 'inserisci il contenuto del tuo articolo'})
        }
        labels = {
            'title': 'titolo',
            'author': 'autore',
            'argument': 'tema',
            'text': 'contenuto'
        }

#class CreaCategoria(forms.ModelForm):
    #class Meta:
        #model = Theme
