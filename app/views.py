from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *


def Topic_forms(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method == 'POST':
        TFDO= TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('topic is created')
        else:
            return HttpResponse('Data is not valid')
    return render (request,'Topic_forms.html',d)

def Webpage_forms(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method == 'POST':
        WFDO= WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['Email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,Email=e)[0]
            WO.save()
            return HttpResponse('Webpage is created')
        else:
            return HttpResponse('Something went wrong')
    return render (request,'Webpage_forms.html',d)

def AccessRecord_forms(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}

    if request.method == 'POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(name=na)
            d=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            AO.save()
            return HttpResponse('AccessRecord is created')
        else:
            return HttpResponse('Something went wrong')
    return render(request,'AccessRecord_forms.html',d)
