from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Sso_Register
from .forms import SsoRegisterPostForm


@login_required(login_url="/?next=/sso_user_register")
def sso_register(request):
    if request.method == "POST":
        form = SsoRegisterPostForm(request.POST, request.FILES)
        if form.is_valid():
            sso_user = form.save(commit=False)
            sso_user.user = request.user
            sso_user.save()
            return redirect('/sso_user_register/')
    else:
        form = SsoRegisterPostForm()
        sso_list = Sso_Register.objects.filter(user=request.user)

    return render(request, 'sso-registration.html', {'form': form, 'sso_list':sso_list})


@login_required(login_url="/?next=/sso_user_register")
def remove_from_sso(request, id):
    Sso_Register.objects.get(id=id).delete()
    return redirect(reverse('sso_register'))


