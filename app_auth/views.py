from django.shortcuts import render, redirect
from django.urls import reverse , reverse_lazy
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


@login_required(login_url= reverse_lazy('login'))
def profile_view(request):
    return render(request , 'app_auth/profile.html')

# Create your views here.
def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request , 'app_auth/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request , username=username , password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request , 'app_auth/login.html' , context= {'error' : 'Пользователь не найден'})
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                form.save()
                username = request.POST.get('username')
                password = request.POST.get('password')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                user = authenticate(request, username=username, password=password , first_name = first_name , last_name = last_name)
                login(request , user)
                return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app_auth/register.html', {'form': form})




