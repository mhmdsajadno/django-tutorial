from django.shortcuts import get_object_or_404, render, redirect
from .models import Book

# Create your views here.
def index(r):
    return redirect('home/')

def home(r):
    books = Book.objects.all()
    return render(r,'home.html',{'books': books})