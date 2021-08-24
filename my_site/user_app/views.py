from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterCustomUserForm


class RegisterUser(CreateView):
    form_class = RegisterCustomUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
