from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic import DetailView

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogDetailView(DetailView):
        model = Post
        template_name = "post_detail.html"