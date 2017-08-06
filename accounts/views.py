from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import HttpResponseRedirect
import logging
from axes.decorators import watch_login
from .forms import SignUpForm
from django.views.generic import FormView
from django.conf import settings
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

print(logger)
@watch_login
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
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
        else:
            login_failed = True

    return render(request, 'accounts/login.html', {'login_failed': login_failed})

class SignUpView(FormView):
    success_url = '/dashboard/'
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def get_initial(self):
        # Force logout.
        logout(self.request)

        return {'time_zone': settings.TIME_ZONE}

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.full_clean()

        if form.is_valid():
            username = form.cleaned_data['username'].replace(' ', '').lower()
            password = form.cleaned_data['password']

            user = User.objects.create(username=username)
            user.email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            # Update the user's settings.
            user.settings.time_zone = form.cleaned_data['time_zone']
            user.settings.save()

            logger.info('New user signed up: %s (%s)', user, user.email)

            # Automatically authenticate the user after user creation.
            user_auth = authenticate(username=username, password=password)
            login(request, user_auth)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

