from django.urls import path, include
from shipping import views


app_name = "shipping"
urlpatterns = [
    path('',views.index,name='index'),
]
