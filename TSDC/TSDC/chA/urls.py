from django.urls import path, include
from chA import views


app_name = "chA"
urlpatterns = [
    path('',views.index,name='index'),
]


