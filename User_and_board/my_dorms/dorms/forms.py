from django import forms
from dorms.models import Context, Comment

class ContextForm (forms.ModelForm) :
    class Meta :
        model = Context
        fields = ['title', 'content']

class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['content',]
        # labels = {
        #     'content' : '답변내용'
        # }