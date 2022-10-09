from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'todoapp1/index.html')
def todos(request):
    return render(request, 'todoapp1/single.html')

def add_categorie(request):
    return render(request, 'todoapp1/add_categorie.html')