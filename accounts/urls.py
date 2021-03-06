from django.urls import path, include
from . import views
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView

)
urlpatterns = [
    path('register/', views.register, name="register"),
    # path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('profile/', views.profile, name="profile"),

    path('password-reset/', PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    
]