from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView

from .forms import CreateUserForm

from datetime import timedelta

from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
# Create your views here.

'''First login view created based on def function'''
def loginPage(request):
    error_message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session.set_expiry(0 if remember_me else timedelta(days=30).seconds)
            login(request, user)
            return redirect ("main-site")
        else:
            error_message = "Błędny login lub hasło spróbuj jeszcze raz."

    context = {
        "error_message" : error_message,
        }
    return render(request, 'Accounts/loginPage.html', context)

'''Second view register page created based on class View '''
class RegisterPage(View):

    def get(self, request):
        form = CreateUserForm()
        context = {
            'form': form,
        }
        return render(request, 'Accounts/registerPage.html', context)
    
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists(): #Checking is EmailAddress is already in Dbase
                form.add_error('email', f'Istnieje już konto z takim adresem email')
            else:
                form.save()
                register_sucees = True
                context = {
                   'register_sucees' : register_sucees,
                }
                return redirect('register_success')
        else:
            return render(request, 'Accounts/registerPage.html', {
                'form': form
            })

class RegisterSucces(TemplateView):
    template_name = 'Accounts/registerSuccess.html'
