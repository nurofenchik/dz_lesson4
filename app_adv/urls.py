from django.urls import path
from .views import hehe
from .views import index
urlpatterns = [path('1', hehe),
               path('',index)
               ]

