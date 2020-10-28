from django.urls import path  
from givmed import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='registration'),
    path('profile/', views.profile, name='profile'),
]