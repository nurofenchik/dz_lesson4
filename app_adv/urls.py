from django.urls import path
from .views import hehe
from .views import index
from .views import test
from .views import test2
from .views import *

urlpatterns = [path('1', hehe),
               path('',index, name = 'index'),
               path('advertisement', advertisement, name = 'advertisement'),
               path('advertisement_post', advertisement_post , name = 'advertisement-post'),
               path('base', base , name = 'base'),
               #path('login', login , name = 'login'),
               #path('profile', profile , name = 'profile'),
               path('register', register , name = 'register'),
               path('top_sellers', top_sellers , name = 'top-sellers'),
               path('test/' , test , name = 'test'),
               path('test2/' ,test2 , name = 'test2'),
               #path('home' , home , name = 'home')
               ]

