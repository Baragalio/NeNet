from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .form import LoginForm

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(data["user"])
            password = data["password"]
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Аутентификация прошла успешно!")
                else:
                    return HttpResponse("Нет такой учётной записи!")
            else:
                return HttpResponse("Неправильный логин!")
    else:
        form = LoginForm()
    return render(request, login.html, {"form":form})
