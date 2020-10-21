from django.shortcuts import render
from .forms import RegistrationForm, InformationForm
from .models import Information

def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        inf_form = InformationForm(request.POST)
        if user_form.is_valid() and inf_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            inf = Information()
            inf.user = new_user
            inf.age = inf_form.cleaned_data['age']
            inf.gender = inf_form.cleaned_data['gender']

            color = ""
            for i in inf_form.cleaned_data['color']:
                color += i

            inf.color = color
            inf.season = inf_form.cleaned_data['season']
            inf.scope = inf_form.cleaned_data['scope']
            inf.purpose = inf_form.cleaned_data['purpose']
            inf.count_fr = inf_form.cleaned_data['count_fr']
            inf.save()
            return render(request, 'registration/registration_success.html')
    else:
        user_form = RegistrationForm()
        inf_form = InformationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form, 'inf_form': inf_form})
