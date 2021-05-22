from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy',views.destroy),
    path('add2',views.add2),
    path('addnumber',views.addnumber),
   
]