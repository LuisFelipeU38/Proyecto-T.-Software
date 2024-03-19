from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'index/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al usuario a la página de inicio de sesión
    else:
        form = CustomUserCreationForm()
    return render(request, 'index/register.html', {'form': form})

