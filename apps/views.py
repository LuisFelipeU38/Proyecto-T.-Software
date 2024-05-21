from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import VideoGame, CustomUser, Order
from django.views import View
from django.views.generic import TemplateView, ListView 
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse

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

class VideoGameIndexView(View): 
    template_name = 'index/index.html' 

    def get(self, request, id): 
        viewData = {} 
        viewData["title"] = "Video games - El Botardo.com" 
        viewData["subtitle"] = "List of games in stock"
        category = request.GET.get('category')  # Obtener la categoría de la solicitud GET
        if category:
            videogames = VideoGame.objects.filter(category=category)
            print(f"Filtrando por categoría: {category}, videojuegos encontrados: {videogames.count()}")
        else:
            videogames = VideoGame.objects.all()
            print(f"Mostrando todos los videojuegos, cantidad: {videogames.count()}")
        viewData["videogames"] = videogames
        viewData["customuser"] = CustomUser.objects.get(id=id)  # Agrega el objeto CustomUser al contexto

        return render(request, self.template_name, viewData)
    
class VideoGameShowView(View): 
    template_name = 'index/show.html' 

    def get(self, request, customuser_id, videogame_id): 
        try:
            customuser_id = int(customuser_id)
            videogame_id = int(videogame_id)
            if videogame_id < 1:
                raise ValueError("VideoGame id must be 1 or greater")
            videogame = get_object_or_404(VideoGame, pk=videogame_id)
            customuser = get_object_or_404(CustomUser, pk=customuser_id)
        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse('profile'))  # Redirigir a la página de inicio si el ID no es válido
        
        viewData = {
            "title": videogame.title + "        Developer        ->",
            "subtitle":  videogame.dev + "   ",
            "videogame": videogame,
            "customuser": customuser,
        }

        return render(request, self.template_name, viewData)
    
class VideoGameListView(ListView):
    model = VideoGame
    template_name = 'videogame_list.html'
    context_object_name = 'videogames'  # This will allow you to loop through 'videogames' in your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'videogames - Online Store'
        context['subtitle'] = 'List of videogames'
        return context
    
def add_order(request, videogame_id, customuser_id):
    if request.method == 'POST':
        # Convertir los IDs a enteros
        customuser_id = int(customuser_id)
        videogame_id = int(videogame_id)
        

        customuser = get_object_or_404(CustomUser, pk=customuser_id)
        videogame = get_object_or_404(VideoGame, pk=videogame_id)
        
        # Crear una nueva instancia de Order
        order = Order.objects.create(
            user_id=customuser,
            videogame_id=videogame
        )
        
        # Guardar la instancia en la base de datos
        order.save()
        
        # Redirigir a alguna página de éxito o a donde desees
        return HttpResponseRedirect(reverse('profile'))
    else:
        # Si el método no es POST, redirigir a alguna página de error o a donde desees
        return HttpResponseRedirect(reverse('profile'))
    
# Función para obtener el carrito desde la sesión
def get_cart(request):
    cart = request.session.get('cart', {})
    return cart

# Función para agregar un producto al carrito
def add_to_cart(request, videogame_id):
    cart = get_cart(request)
    videogame = get_object_or_404(VideoGame, id=videogame_id)
    if str(videogame_id) in cart:
        cart[str(videogame_id)]['quantity'] += 1
    else:
        cart[str(videogame_id)] = {
            'title': videogame.title,
            'price': videogame.price,
            'quantity': 1,
        }
    request.session['cart'] = cart
    return redirect('cart')

# Función para eliminar un producto del carrito
def remove_from_cart(request, videogame_id):
    cart = request.session.get('cart', {})

    if str(videogame_id) in cart:
        del cart[str(videogame_id)]
        request.session['cart'] = cart

    return redirect('cart')

# Función para ver el carrito
def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for item_id, item_data in cart.items():
        cart_items.append({
            'id': item_id,
            'title': item_data['title'],
            'price': item_data['price'],
            'quantity': item_data['quantity']
        })
    return render(request, 'index/cart.html', {'cart': cart_items})