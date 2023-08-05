from django.urls import path
from .views import HUY
from .views import index
urlpatterns = [path('1', HUY),
               path('',index)
               ]

