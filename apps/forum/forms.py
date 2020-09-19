from .models import Topic, Post
from django import forms
import datetime


class CreateTopic(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateTopic, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Topic
        fields = ("name", "slug", "posting")

class CreatePost(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Post
        fields = ("name", "post")