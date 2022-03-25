from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'chC/index.html',
        {
            'title':'chC Home Page',
        }
    )