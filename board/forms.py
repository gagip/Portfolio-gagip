from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

        # Form 요소의 css 적용
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'class': 'comment-input',
                },
            )
        }
