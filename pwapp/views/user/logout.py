from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import  RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

class LogoutView(LoginRequiredMixin, RedirectView):
    pattern_name = 'login'
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "Logged out successfully!")
        return super(LogoutView, self).get(request, *args, **kwargs)
