from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    return HttpResponse('Пользователь не найден!')
            else:
                return HttpResponse('Неправильный логин!')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})