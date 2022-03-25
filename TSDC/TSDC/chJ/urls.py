from django.urls import path, include
from chJ import views


app_name = "chJ"
urlpatterns = [
    path('',views.index,name='index'),
    path('stock2881',views.stock2881,name='stock2881'),
    path('stock2330',views.stock2330,name='stock2330'),
]



