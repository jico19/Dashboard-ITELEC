from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserLoginForm.as_view(), name="login_view"),
    path('register/', views.UserRegisterFormView.as_view(), name="register_view"),
    path('logout/', views.LogoutView.as_view(), name="logout_view"),
]
