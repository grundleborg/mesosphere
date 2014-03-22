from django import forms
from django.forms import ModelForm

from datetime import datetime

from mesoblog.models import Article, Comment

class CommentForm(ModelForm):
    article = forms.ModelChoiceField(label="",
                                     queryset=Article.objects.all(),
                                     widget=forms.HiddenInput())
    parent = forms.ModelChoiceField(label="",
                                    queryset=Comment.objects.all(),
                                    widget=forms.HiddenInput(),
                                    required=False)
   
    class Meta:
        model = Comment
        fields = ['name', 'email', 'site', 'contents', 'article', 'parent']
    
    def save(self, commit=True):
        i = super(CommentForm, self).save(commit=False)
        i.posted = datetime.now()
        i.save()
        return i


