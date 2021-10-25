from django.views.generic import ListView
from .models import SomeModel

class BlogListView(ListView):
    model = SomeModel
    template_name = 'blog.html'
    context_object_name = 'posts'

# Create your views here.
