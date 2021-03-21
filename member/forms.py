from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Profile

class SignupForm(forms.ModelForm):
    ''' 회원가입 양식 '''
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 
                    'first_name', 'last_name', 'email']

    def clean_password2(self):
        ''' 비밀번호 비교 및 반환 '''
        cd = self.cleaned_data
        # 비밀번호가 서로 일치하지 않는다면, 에러를 보낸다.
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 서로 일치하지 않습니다.')
        return cd['password2']


class ProfileForm(forms.ModelForm):
    ''' 프로필 양식 '''
    
    class Meta:
        model = Profile
        fields = ['picture', 'nickname', 'introduce', ]




class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')     # form에 입력된 password 
        confirm_password = self.user.password       # 현재 사용자의 password
        
        # 비밀번호 비교
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
