from django.urls import path, include
from chH import views


app_name = "chH"
urlpatterns = [
    path('',views.index,name='index'),
]



