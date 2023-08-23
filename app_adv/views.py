from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Advertisement # импортировал модель обьявления
from .forms import AdvertisementForm
from django.urls import reverse



# функция представление
def index(request):
    advertisements =  Advertisement.objects.all() # все записи
    context = {'advertisements': advertisements}
    return render(request, "index.html", context)
#def index(request):
    #return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def advertisement(request):
    return render(request, 'advertisement.html')
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            Advertisement = form.save(commit=False)
            Advertisement.user = request.user
            Advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
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