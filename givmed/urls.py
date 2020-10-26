from django.urls import path  
from givmed import views

urlpatterns = [
    path('', views.index,name='index'),
]