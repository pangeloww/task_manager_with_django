from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from aboutus.forms import BulletinEmailForm


# Create your views here.

class AboutUsView(TemplateView):
    template_name = 'aboutus/about_us.html'


def gather_emails_for_bulletins(request):
    form = BulletinEmailForm()
    if request.method == 'POST':
        form = BulletinEmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'aboutus/bulletin.html/', context)
