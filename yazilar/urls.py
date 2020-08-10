from django.urls import path
from . import views

urlpatterns = [
    path('', views.YazıView.as_view(), name='yazi'),
    path('yaz/', views.yazdır, name='yaz'),
]