from django.contrib.auth.forms import UserChangeForm
# 유저 모델을 가져오기 위한
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username',)
    