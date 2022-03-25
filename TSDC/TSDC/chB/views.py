from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'chB/index.html',
        {
            'title':'chB Home Page',
        }
    )