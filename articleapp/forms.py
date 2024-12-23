from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'editable text-left', 'style': 'height: auto;'}),
        label='내용'  # 내용으로 변경
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        required=False,
        label='프로젝트'  # 프로젝트로 변경
    )

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        labels = {
            'title': '제목',  # 제목으로 변경
            'image': '사진',  # 사진으로 변경
        }
