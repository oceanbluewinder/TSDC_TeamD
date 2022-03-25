from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'chI/index.html',
        {
            'title':'chI Home Page',
        }
    )