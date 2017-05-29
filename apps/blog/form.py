from django.forms import ModelForm, Textarea
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('article_title', 'category', 'article_text')
        widgets = {
            'article_text': Textarea(attrs={'cols': 80, 'rows': 10}),
        }
