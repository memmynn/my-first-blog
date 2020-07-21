from django.urls import path
from . import views

urlpatterns = [
    path('', views.yazi, name='yazi'),
]