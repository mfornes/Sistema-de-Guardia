from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

def guard_plan_page(request):
	return render(request, "guard_plan_page.html")