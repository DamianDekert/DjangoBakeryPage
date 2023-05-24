from django import forms

from .models import UsersMessages

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UsersMessages
        fields = "__all__"

        labels = {
            'first_name' : 'Imię',
            'last_name' : 'Nazwisko',
            'email' : 'Adres email',
            'message' : 'Wiadomość',
        }
