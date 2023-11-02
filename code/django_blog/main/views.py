from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Post



def index(request):
    return render(request, 'main/index.html')


class PostsList(ListView):
    model = Post
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = "Posts List"
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = f"Post: {self.get_object().title}"
        return context



