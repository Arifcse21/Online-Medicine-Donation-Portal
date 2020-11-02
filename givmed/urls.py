from django.urls import path  
from givmed import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='givmed/login.html'), name='login'),

]