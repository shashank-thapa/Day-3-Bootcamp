from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    d={
        'names':['Shashank','Kritika','Nischal']
    }

    return render(request, 'scraper_app/index.html', d)

def about(request):
    return render(request, 'scraper_app/about.html')
