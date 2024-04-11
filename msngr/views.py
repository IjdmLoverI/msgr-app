from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from msngr.forms import SearchForm, UserForm
from msngr.models import Conversation


@login_required
def index(request):
    num_conversations = Conversation.objects.count()
    num_users = User.objects.count()

    context = {
        "num_conversations": num_conversations,
        "num_users": num_users
    }
    return render(request, "msngr/index.html", context=context)


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 10
    template_name = "msngr/users_list.html"

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("search", "")
        context["search_form"] = SearchForm(initial={"search": username})
        return context

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.GET.get("search")
        if username is not None:
            return queryset.filter(username__icontains=username)
        return queryset


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "msngr/user_detail.html"


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserForm
    template_name = "msngr/user_form.html"

    def get_success_url(self):
        return reverse_lazy("msngr:user-detail", kwargs={'pk': self.kwargs['pk']})


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("login")
    template_name = "msngr/user_confirm_delete.html"


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy("login")
    template_name = "msngr/user_form.html"
