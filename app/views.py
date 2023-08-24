from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    QSTO = Topic.objects.all()
    d = {'QSTO' : QSTO }
    return render(request, 'display_topics.html', d)


def display_webpages(request):
    QSWO = WebPage.objects.all()
    d = {'QSWO' : QSWO }
    return render(request, 'display_webpages.html', d)

def display_accessrecords(request):
    QSARO = AccessRecord.objects.all()
    d = {'QSARO': QSARO}
    return render(request,'display_accessrecords.html', d)