from django.urls import path
from app1.views import *
app_name='jyothika'
urlpatterns = [
    path('chandramukhi/',chandramukhi,name='chandramukhi'),

]