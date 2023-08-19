from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def advertisement(request):
    return render(request, 'advertisement.html')
def advertisement_post(request):
    return render(request, 'advertisement-post.html')
def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')
def register(request):
    return render(request, 'register.html')
def top_sellers(request):
    return render(request, 'top-sellers.html')
def hehe(request):
    return HttpResponse('Успешно')

def test(request):
    return render(request, 'test.html')
def test2(request):
    return render(request, 'test2.html')