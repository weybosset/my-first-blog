#from django.shortcuts import render

from django.http import HttpResponse
from books.models import Books

def index(request):
	books_list = Books.objects.all()
	return HttpResponse(books_list)