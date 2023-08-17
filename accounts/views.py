from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import CreateAccountForm, EditAccountForm
from accounts.models import User


# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = CreateAccountForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Set user as inactive initially
            user.save()

            return redirect('home')  # Redirect to a success page

        return render(request, 'accounts/register.html', {'form': form})


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'


class LogoutUserView(LogoutView):
    template_name = 'accounts/logout_page.html'


def edit_profile(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('edit profile', pk=request.user.pk)

    else:
        form = EditAccountForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)
