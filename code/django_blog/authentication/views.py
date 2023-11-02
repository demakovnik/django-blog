from django.views.generic import CreateView, DetailView, ListView

from authentication.forms import UserCreateForm
from authentication.models import User


class UsersList(ListView):
    model = User
    # context_object_name = 'animals'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = "Users List"
        return context


class UserCreateView(CreateView):
    model = User
    success_url = '/'
    form_class = UserCreateForm



    def form_valid(self, form):
        form.instance.is_superuser = 1
        return super().form_valid(form)





class UserDetailView(DetailView):
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = f"User name: {self.get_object().username}"
        return context
