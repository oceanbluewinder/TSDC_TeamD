from django.urls import path, include
from financial import views


app_name = "financial"
urlpatterns = [
    path('',views.index,name='index'),
]

