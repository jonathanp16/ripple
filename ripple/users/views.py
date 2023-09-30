from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView
from .models import Reference

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name", "bio"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


class UserReferenceListView(ListView):
    model = Reference
    template_name = 'users/references.html'
    context_object_name = 'references'
    
    def get_queryset(self):
        user_id = self.kwargs['pk']  # Retrieve the user's ID from the URL
        user = User.objects.get(id=user_id)
        return Reference.objects.filter(user=user)


class ReferenceDetailView(LoginRequiredMixin, DetailView):
    model = Reference
    slug_field = "id"
    slug_url_kwarg = "id"

user_detail_view = UserDetailView.as_view()
user_update_view = UserUpdateView.as_view()
user_redirect_view = UserRedirectView.as_view()
user_references_view = UserReferenceListView.as_view()
reference_detail_view = ReferenceDetailView.as_view()
