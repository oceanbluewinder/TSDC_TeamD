from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'chG/index.html',
        {
            'title':'chG Home Page',
        }
    )