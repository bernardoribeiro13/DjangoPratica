from django.urls import path
from galeria.views import titulo

urlpatterns = [
    path('', titulo),
    
]