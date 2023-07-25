from django.urls import path
from .views import index
from .views import app_lesson_4
urlpatterns = [path('', index),
               path('lesson4', app_lesson_4)
               ]

