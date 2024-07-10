from django.urls import path
from .views import book_create_view, book_success_view, home_view
urlpatterns = [
    path('', home_view, name='home'), # Add this line
    path('create/', book_create_view, name='book_create'),
    path('success/', book_success_view, name='book_success'),
]