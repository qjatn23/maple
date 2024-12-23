from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
        labels = {
            'image': '프로필 이미지',
            'nickname': '닉네임',
            'message': '메시지',
        }
