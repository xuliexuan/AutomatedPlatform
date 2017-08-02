from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import HttpResponseRedirect

def login_view(request):
    # Force logout.
    logout(request)
    username = password = ''

    # Flag to keep track whether the login was invalid.
    login_failed = False
    if request.POST:
        username = request.POST['username'].replace(' ', '').lower()
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
        else:
            login_failed = True

    return render(request, 'accounts/login.html', {'login_failed': login_failed})