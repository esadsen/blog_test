from django import forms
from .models import Article

INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')  # author alanını buradan kaldırıyoruz
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'content': forms.Textarea(attrs={'class': INPUT_CLASSES}),
        }