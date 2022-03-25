from django.urls import path, include
from chD import views


app_name = "chD"
urlpatterns = [
    path('',views.index,name='index'),
]



