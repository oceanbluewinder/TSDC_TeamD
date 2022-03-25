"""
Definition of urls for TSDC.
"""
"""
from datetime import datetime
from django.urls import path, include #add "include"
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import View
from app import forms, views
from food import""
"""

from django.conf.urls import url,include
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from food import views #食品
from financial import views #金融
from shipping import views #航運
from chA import views #chA專題動機
from chB import views #chB專題目標
from chC import views #chC專題行程
from chD import views #chD整理股票相關遭遇的困難
from chE import views #chE爬蟲相關遭遇的困難
from chF import views #chF撰寫網站遭遇的困難
from chG import views #chG小組合作遭遇的困難
from chH import views #chH專題展望
from chI import views #chI文章範例一
from chJ import views #chJ文章範例二

from app import forms, views #初始app

from django.urls import include, path

 

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    url(r'^food/', include('food.urls')),#食品業
    url(r'^financial/', include('financial.urls')),#金融業
    url(r'^shipping/', include('shipping.urls')),#航運業
    url(r'^chA/', include('chA.urls')),#chA專題動機
    url(r'^chB/', include('chB.urls')),#chB專題目標
    url(r'^chC/', include('chC.urls')),#chC專題行程
    url(r'^chD/', include('chD.urls')),#chD整理股票相關遭遇的困難
    url(r'^chE/', include('chE.urls')),#chE爬蟲相關遭遇的困難
    url(r'^chF/', include('chF.urls')),#chF撰寫網站遭遇的困難
    url(r'^chG/', include('chG.urls')),#chG小組合作遭遇的困難
    url(r'^chH/', include('chH.urls')),#chH專題展望
    url(r'^chI/', include('chI.urls')),#chI文章範例一
    url(r'^chJ/', include('chJ.urls')),#chJ文章範例二
]
