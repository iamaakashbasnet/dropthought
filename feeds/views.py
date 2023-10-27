from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Thought


class ThoughtListView(ListView):
    model = Thought
    template_name = 'feeds/home.html'
    context_object_name = 'thoughts'
    ordering = '-date_posted'
    paginate_by = 10


class ThoughtCreateView(LoginRequiredMixin, CreateView):
    model = Thought
    fields = ['content',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ThoughtDetailView(DetailView):
    model = Thought
    context_object_name = 'thought'


class ThoughtUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thought
    fields = ['content',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        thought = self.get_object()
        if self.request.user == thought.author:
            return True
        return False


class ThoughtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thought
    success_url = '/home'
    context_object_name = 'thought'

    def test_func(self):
        thought = self.get_object()
        if self.request.user == thought.author:
            return True
        return False
