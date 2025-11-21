from django.urls import path
from .views import SignUpView, logout_view
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Using Django's built-in LoginView
    path('logout/', logout_view, name='logout'),  # Using Django's built-in LogoutView
]
