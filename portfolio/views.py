from django.shortcuts import render

# Create your views here.


# Asegurate de que el nombre sea exactamente 'home_portfolio' con el guion bajo
def home_portfolio(request):
    return render(request, 'portfolio/index.html')
