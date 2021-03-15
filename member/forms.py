from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    ''' 회원가입 양식 '''
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        ''' 비밀번호 비교 및 반환 '''
        cd = self.cleaned_data
        # 비밀번호가 서로 일치하지 않는다면, 에러를 보낸다.
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 서로 일치하지 않습니다.')
        return cd['password2']