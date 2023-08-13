from django.urls import path
from .views import hehe
from .views import index
from .views import test
from .views import test2
urlpatterns = [path('1', hehe),
               path('',index),
               path('test/' , test , name = 'test'),
               path('test2/' ,test2 , name = 'test2')
               ]

