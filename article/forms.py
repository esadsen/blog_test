from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget

INPUT_CLASSES='w-full py-4 px-6 rounded-xl border' # Tailwind ile class ekledim.

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')  
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter the title of the article'
            }),
            'content': CKEditorWidget(),
        }
        
class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')  
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'content': CKEditorWidget(),
        }