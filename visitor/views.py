from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Visitor_Register
from .forms import VisitorForm
from django.http import HttpResponseForbidden


def visitor_registration(request):
    visits = Visitor_Register.objects.filter(user=request.user)
    return render(request, 'visitor-registration.html', {'visits':visits})

def add_visitor(request):
    if request.method == "POST":
        form = VisitorForm(request.POST, request.FILES)
        if form.is_valid():
            print("========")
            visitor = form.save(commit=False)
            visitor.user = request.user
            visitor.save()
            return redirect("/visitor_registration/")
    else:
        form = VisitorForm()
        
    return render(request, 'add-visitor.html', {'form': form})

def edit_visitor(request, id=None):
    if id:
        visitor = get_object_or_404(Visitor_Register, pk=id)
        if visitor.user != request.user:
            return HttpResponseForbidden()
    else:
        visitor = Visitor_Register.objects.filter(user=request.user)

    form = VisitorForm(request.POST or None, instance=visitor)
    if form.is_valid():
        advert = form.save()
        return redirect("/visitor_registration/")
#    else:
#        form = VisitorForm(instance=visitor)
    return render(request, 'add-visitor.html', {'form': form})

def remove_visitor(request, id):
    Visitor_Register.objects.get(id=id).delete()
    return redirect(reverse('visitor_registration'))