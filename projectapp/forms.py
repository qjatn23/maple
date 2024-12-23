from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'description']
        labels = {
            'image': '이미지',  # 이미지로 변경
            'title': '제목',  # 프로젝트 제목으로 변경
            'description': '설명',  # 설명으로 변경
        }
