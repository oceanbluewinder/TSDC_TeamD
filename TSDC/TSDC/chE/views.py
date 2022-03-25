from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'chE/index.html',
        {
            'title':'chE Home Page',
        }
    )