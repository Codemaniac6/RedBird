from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'templates/user_registration.html'

    def get_success_url(self):
        return reverse('home')
