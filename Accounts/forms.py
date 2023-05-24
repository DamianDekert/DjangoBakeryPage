from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import password_validation

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
    label="Hasło",
    widget=forms.PasswordInput,
    help_text=password_validation.password_validators_help_text_html(),
)
    password2 = forms.CharField(
    label="Powtórz hasło",
    widget=forms.PasswordInput,
)
    username = forms.CharField(
    label="Nazwa użytkownika",
)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name'    : 'Imię',
            'last_name'     : 'Nazwisko',
            'email'         : 'email',
        }
    