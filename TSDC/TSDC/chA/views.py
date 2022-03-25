from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'chA/index.html',
        {
            'title':'chA Home Page',
        }
    )