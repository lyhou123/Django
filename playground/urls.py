# we map ulr to see results
from django.urls import path

from . import views

# URL config

urlpatterns = [
    path('', views.room),
    path('test/', views.say_hello, name='room'),

]
