from typing import Dict, Any

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest

from .forms import CustomLoginForm, RegisterForm
from Blog.models import BlogModel


class LoginPage(generic.edit.FormView):
    """ Login page view """

    form_class = CustomLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('landing_page')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """ Redirect user from login page if is_authenticated """

        if self.request.user.is_authenticated:
            return redirect('/')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: CustomLoginForm) -> Dict[str, Any]:

        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, "You have logged in")
        else:
            messages.error(self.request, "Username or password incorrect")

        return super().form_valid(form)

    def form_invalid(self, form: CustomLoginForm) -> Dict[str, Any]:

        messages.error(self.request, form.errors)

        return redirect('landing-page')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()

        return context


class AccountPage(LoginRequiredMixin, generic.list.ListView):
    """ List articles on user account """

    model = BlogModel
    template_name = 'users/account.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('account')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        articles = BlogModel.objects.filter(owner=self.request.user.id)

        context['articles'] = articles
        # breakpoint()
        return context


class Register(generic.edit.FormView):
    template_name = 'Users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('landing_page')

    def form_valid(self, form: RegisterForm) -> Dict[str, Any]:

        user = form.save()

        if user is not None:
            login(self.request, user)
            messages.info(self.request, "account created")

        return super(Register, self).form_valid(form)

    def form_invalid(self, form: RegisterForm) -> Dict[str, Any]:

        messages.error(self.request, form.errors)

        return super(Register, self).form_invalid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Dict[str, Any]:

        if self.request.user.is_authenticated:
            return redirect('/')

        return super().dispatch(request, *args, **kwargs)
