from django.urls import path, include
from chE import views


app_name = "chE"
urlpatterns = [
    path('',views.index,name='index'),
]



