from django.urls import path, include
from chC import views


app_name = "chC"
urlpatterns = [
    path('',views.index,name='index'),
]



