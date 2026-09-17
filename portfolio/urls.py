from django.urls import path
from . import views

urlpatterns = [
    # El primer argumento vacío '' significa que reacciona a la raíz (http://127.0.0)
    path('', views.home_portfolio, name='portfolio_home'),
]
