from django.urls import path, include
from chG import views


app_name = "chG"
urlpatterns = [
    path('',views.index,name='index'),
]



