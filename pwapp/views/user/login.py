from django.views.generic import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
    success_url =  reverse_lazy("homepage")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
        if user is not None:
            login(self.request, form.get_user())
            return HttpResponseRedirect(self.get_success_url())
        return super(LoginView, self).form_valid(form)