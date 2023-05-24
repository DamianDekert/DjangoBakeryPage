from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View, TemplateView

from .forms import UserMessageForm

# Create your views here.
class MainSite(View):
    
    def get(self, request):
        form = UserMessageForm
        success_message =   """               
                            Przeanalizujemy Państwa zapytanie i wrócimy
                            z odpowiedzią najszybciej jak to możliwe 😊. 
                            Aby umilić oczekiwanie zachęcamy do zapoznania
                            się z pełnym słodkim asortymentem.
                            """
        
        return render(request, 'CoreApp/main.html', {
            'form' : form,
            'success_message' : success_message,
            'form_submitted' : request.session.get('form_submitted', False)
        })
    
    def post(self, request):
        form = UserMessageForm(request.POST)

        if form.is_valid():
            form.save()
            request.session["form_submitted"] = True #Cookie session set at 120s
            url = reverse('main-site') + '#contact'
            return redirect (url)
        else :
            return render(request, 'CoreApp/main.html', {
                'form' : form,
            })

class PrivacyPolicy(TemplateView):
    template_name = "CoreApp/privacy_policy.html"