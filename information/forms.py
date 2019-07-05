from django import forms
from .models import Information

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information 
        fields = ['title', 'name', 'body']
        labels = {
            "title" : "카테고리",
            "name" : "이름",
            "body" : "후기"
        }
        widgets = {
            'body':forms.Textarea(attrs={'rows':20, 'cols':137}),
        }