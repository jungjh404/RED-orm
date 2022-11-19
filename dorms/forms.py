from django import forms
from dorms.models_copy import Context, Comment, Context_info, Comment_info, Context_free, Comment_free, Context_trade, Comment_trade, Comment_copur, Context_copur

class ContextForm (forms.ModelForm) :
    class Meta :
        model = Context
        fields = ['title', 'content']

class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['content']
        labels = {
            'content' : '답변내용'
        }

class ContextInfoForm (forms.ModelForm) :
    class Meta :
        model = Context_info
        fields = ['title', 'content']

class CommentInfoForm(forms.ModelForm) :
    class Meta :
        model = Comment_info
        fields = ['content']
        labels = {
            'content' : '답변내용'
        }

class ContextFreeForm (forms.ModelForm) :
    class Meta :
        model = Context_free
        fields = ['title', 'content']

class CommentFreeForm(forms.ModelForm) :
    class Meta :
        model = Comment_free
        fields = ['content']
        labels = {
            'content' : '답변내용'
        }

class ContextTradeForm (forms.ModelForm) :
    class Meta :
        model = Context_trade
        fields = ['title', 'content']

class CommentTradeForm(forms.ModelForm) :
    class Meta :
        model = Comment_trade
        fields = ['content']
        labels = {
            'content' : '답변내용'
        }

class ContextCopurForm (forms.ModelForm) :
    class Meta :
        model = Context_copur
        fields = ['title', 'content']

class CommentCopurForm(forms.ModelForm) :
    class Meta :
        model = Comment_copur
        fields = ['content']
        labels = {
            'content' : '답변내용'
        }