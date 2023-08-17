from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "base.html"

def custom_404(request, exception):
    return render(request, '404.html', status=404)