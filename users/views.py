from django.shortcuts import render
from django.contrib import messages, auth
from users.forms import UserLoginForm, UserRegistrationForm, changePassForm
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

@login_required(login_url='/login?next=profile')
def profile(request):
    user = User.objects.all().order_by('-created_date')
    return render(request, "profile.html", {'user': user})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username_or_email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and 'next' in request.GET:
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('sso_register'))
            else:
                form.add_error(None, "Your username or password was not recognised")

    else:
        # this handles the initial get request
        # return a blank form for user to login
        form = UserLoginForm()

    # prepare args to pass to render function
    #   form:   this is the form which will be rendered to html (UserLoginForm)
    #   next:   if the url of the request included a next query string '?next=' pass it to the form
    #           so that it can be included in the url when the form is resubmitted
    #           see handling of post method: next = request.GET['next']
    args = {'form': form, 'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def change_password(request):
    if request.user.is_authenticated:

        form = changePassForm(request.POST or None)

        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        re_new_password = request.POST.get("re_new__password")

        if request.POST.get("old_password"):

            user = User.objects.get(username= request.user.username)

            #User entered old password is checked against the password in the database below.
            if user.check_password('{}'.format(old_password)) == False:
                form.set_old_password_flag()

        if form.is_valid():

            user.set_password('{}'.format(new_password))
            user.save()
            update_session_auth_hash(request, user)

            return redirect('change_password')

        else:
            return render(request, 'change-password.html', {"form": form})

    else:
        return redirect('login')
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('login'))



