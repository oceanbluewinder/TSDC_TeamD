from django.urls import path, include
from chB import views


app_name = "chB"
urlpatterns = [
    path('',views.index,name='index'),
]


