from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class VideoGameSearchForm(forms.Form):
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('adventure', 'Adventure'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    min_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    max_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    developer = forms.CharField(max_length=255, required=False)
    min_rating = forms.IntegerField(min_value=1, max_value=5, required=False)