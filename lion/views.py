from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"nome": "João","cachorros": ["Mel","Tobias","Belinha","Cacau","Radija","Thor"]}
    return render(request, 'index.html', context)