from django.urls import path 
from . import views 
urlpatterns = [ 
	path('', views.prime_numbers, name='prime_numbers'), 
]