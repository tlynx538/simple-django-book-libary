from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from .models import Books 
# Create your views here.
def index(request):
    book_names = Books.objects.all().values()
    context = {'book_names': book_names}
    return render(request, 'index.html', context)

def add(request):
    return render(request,'add.html')

def add_book(request):
    book_name = request.POST['book_name']
    book = Books(book_name=book_name)
    book.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    book = Books.objects.get(id=id)
    context = {
        'book' : book
    }
    return render(request, 'update.html', context)

def update_book(request,id):
    book_name = request.POST["book_name"]
    book = Books.objects.get(id=id)
    book.book_name = book_name
    book.save()
    return HttpResponseRedirect(reverse('index'))
    
    
