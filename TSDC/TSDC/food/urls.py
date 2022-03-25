from django.urls import path, include
from food import views


app_name = "food"
urlpatterns = [
    path('',views.index,name='index'),
    path('stock',views.stock,name='stock'),
]
