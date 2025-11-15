from django.urls import path
from .views import SignUpView  # Import your views here
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Using Django's built-in LoginView
    path('logout/', LogoutView.as_view(), name='logout'),  # Using Django's built-in LogoutView
]