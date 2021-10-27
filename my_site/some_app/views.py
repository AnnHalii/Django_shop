from django.views.generic import ListView, View
from .models import SomeModel
from django.http import HttpResponseRedirect
from .producer import publish
from datetime import datetime


class BlogListView(ListView):
    model = SomeModel
    template_name = 'blog.html'
    context_object_name = 'posts'


class RegisterClickView(View):
    def get(self, request, *args, **kwargs):
        data = {'username': request.user.username, 'timestamp': datetime.timestamp(datetime.now())}
        publish(data)
        return HttpResponseRedirect('/')
