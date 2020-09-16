from .models import Topic, Post
from django import forms
import datetime


class CreateTopic(forms.ModelForm):
    ## change the widget of the date field.
    # publish_time = forms.DateField(
    #     # change the range of the years from 1980 to currentYear - 5
    #     widget=forms.SelectDateWidget()
    # )

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