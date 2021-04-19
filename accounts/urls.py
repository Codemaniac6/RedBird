from django.urls import path
from .views import UserRegistrationView

app_name = 'accounts'

urlpatterns = [
    path('new-user/', UserRegistrationView.as_view(), name='user_registration'),
]
