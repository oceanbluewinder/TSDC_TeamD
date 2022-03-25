from django.urls import path, include
from chI import views


app_name = "chI"
urlpatterns = [
    path('',views.index,name='index'),
]



