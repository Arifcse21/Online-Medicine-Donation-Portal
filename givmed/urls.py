from django.urls import path  
from givmed import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('register/', views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='givmed/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='givmed/password_reset.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='givmed/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='givmed/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='givmed/password_reset_complete.html'),name='password_reset_complete'),
                            




]