from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money', views.colgold),
    path('reset',views.reset),
]