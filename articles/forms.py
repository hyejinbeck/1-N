from django import forms
from .models import Article ,Comment # ,Comment추가

class ArticleForm(forms.ModelForm): 

    class Meta: 
        model = Article 
        fields = '__all__'

class CommentForm(forms.ModelForm): 

    class Meta: 
        model = Comment 
        # fields = '__all__'   # Comment에 있는 모든 값을 보여줘
        fields = ('content',)   # content만 보여줄래 
                               # fields는 추가 
        # exclude = ('제외되는 모델')
        # fields = ('보여지는 모델')