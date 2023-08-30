from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Advertisement # импортировал модель обьявления
from .forms import AdvertisementForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse , reverse_lazy


# функция представление
def index(request):
    advertisements =  Advertisement.objects.all() # все записи
    context = {'advertisements': advertisements}
    return render(request, "app_adv/index.html", context)
#def index(request):
    #return render(request, 'index.html')
def base(request):
    return render(request, 'app_adv/base.html')
def advertisement(request):
    return render(request, 'app_adv/advertisement.html')
@login_required(login_url = reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            Advertisement = form.save(commit=False)
            Advertisement.user = request.user
            Advertisement.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_adv/advertisement-post.html', context)
#def login(request):
    #return render(request, 'app_auth/login.html')

def register(request):
    return render(request, 'app_auth/register.html')
def top_sellers(request):
    return render(request, 'app_adv/top-sellers.html')
def hehe(request):
    return HttpResponse('Успешно')

def test(request):
    return render(request, 'app_adv/test.html')
def test2(request):
    return render(request, 'app_adv/test2.html')