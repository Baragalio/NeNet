from django.shortcuts import render
from registration.forms import RegistrationForm, InformationForm
from registration.models import Information
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def edit(request):
    if request.method == 'POST':
        name = User.objects.get(pk=request.user.id).username
        Information.objects.get_or_create(user=request.user)
        inf_form = InformationForm(instance=request.user.information, data=request.POST)
        if inf_form.is_valid():
            inf_form.save()
    else:
        name = User.objects.get(pk=request.user.id).username
        inf_form = InformationForm(instance=request.user.information)
    return render(request, "settings.html", {"username":name, "inf_form": inf_form})

