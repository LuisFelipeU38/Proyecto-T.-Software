from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'index/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'index/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Después de registrar al usuario, redirigirlo a la página de inicio de sesión
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'index/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'index/profile.html')
