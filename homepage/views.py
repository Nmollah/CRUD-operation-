from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome bro in home page</h1> <a href='/contact/'>Contact</a> <a href='/about/'>About</a> ")

def about(request):
    return HttpResponse("<h1> Welcome bro in about page</h1> <a href='/contact/'>Contact</a> <a href='/home/'>Home</a> ")


def contact (request):
    return HttpResponse("<h1> Welcome bro contact page</h1> <a href='/home/'>Home</a> <a href='/about/'>About</a> ")