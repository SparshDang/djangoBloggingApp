from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView, FormView

from authApp.forms import SignInForm
# Create your views here.


class LoginPageView(LoginView):
    template_name = 'authApp/login.html'


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))


class AccountView(DetailView):
    model = User
    template_name = 'authApp/userDetail.html'
    context_object_name = 'user'


class AccountCreateView(FormView):
    form_class = SignInForm
    success_url = '/'
    template_name = "authApp/signIn.html"

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']
        newUser = User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name, password=password)
        newUser.save()

        login(self.request, newUser)
        return super().form_valid(form)


@login_required
def deleteUser(request):
    request.user.delete()
    return HttpResponseRedirect(reverse('auth:login'))
