from django.views.generic import TemplateView
from django.shortcuts import redirect


class WelcomeView(TemplateView):
    template_name = 'welcome.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('feeds-home')

        return super().get(request, *args, **kwargs)
