from django.urls import path, include
from chF import views


app_name = "chF"
urlpatterns = [
    path('',views.index,name='index'),
]



