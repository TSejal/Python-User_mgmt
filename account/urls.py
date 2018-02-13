from django.conf.urls import  patterns,include, url
from django.contrib import admin
from user_mgmt import settings
from account.views import *


print("*********url************")
urlpatterns = patterns('',
    url(r'^register/$', account_register, name='register'),
    url(r'^login/$', account_login, name='login'),
    url(r'^home/$', account_home, name='home'),
    url(r'^logout/$', account_logout, name='logout'), 
    #url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/login/'}),
)