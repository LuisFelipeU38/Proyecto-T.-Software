from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import VideoGameIndexView, VideoGameShowView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='index/login.html'), name='login'),
    path('index/<str:id>', VideoGameIndexView.as_view(), name='index'),  
    path('show/<int:customuser_id>/<int:videogame_id>/', VideoGameShowView.as_view(), name='show'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),  # Ruta para ver el carrito
    path('cart/add/<int:videogame_id>/', views.add_to_cart, name='add_to_cart'),  # Ruta para agregar al carrito
    path('cart/remove/<int:videogame_id>/', views.remove_from_cart, name='remove_from_cart'),  # Ruta para eliminar del carrito
    path('checkout/', views.checkout, name='checkout'),  # Ruta para la vista de checkout
    path('order_success/', views.order_success, name='order_success'),
    # path('random_game/', views.random_game_recommendation, name='random_game_recommendation'),  # Ruta para la recomendación aleatoria
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)