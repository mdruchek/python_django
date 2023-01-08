from django.forms import ModelForm
from app_news.models import News, Comment


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'activity']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'text']
