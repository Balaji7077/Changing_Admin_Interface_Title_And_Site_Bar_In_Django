from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField()

class WebpageForm(forms.Form):
    TL=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=TL)
    name=forms.CharField()
    url=forms.URLField()
    Email=forms.EmailField() 

class AccessRecordForm(forms.Form):
    WL=[[wo.name,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=WL)
    date=forms.DateField()
    author=forms.CharField()