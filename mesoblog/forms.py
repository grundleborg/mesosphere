import floppyforms as forms

from datetime import datetime

from mesoblog.models import Article, Comment

class CommentForm(forms.ModelForm):
    article = forms.ModelChoiceField(label="",
                                     widget=forms.HiddenInput(),
                                     queryset=Article.objects.all())
    parent = forms.ModelChoiceField(label="",
                                    widget=forms.HiddenInput(),
                                    queryset=Comment.objects.all(),
                                    required=False)
   
    class Meta:
        model = Comment
        fields = ['name', 'email', 'site', 'contents', 'article', 'parent']
        widgets = {
                'name': forms.TextInput,
                'email': forms.EmailInput,
                'site': forms.URLInput,
                'contents': forms.Textarea,
        }
    
    def save(self, commit=True):
        i = super(CommentForm, self).save(commit=False)
        i.posted = datetime.now()
        i.save()
        return i


