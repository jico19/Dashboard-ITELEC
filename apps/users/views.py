from django.views import generic, View
from . import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


class UserRegisterFormView(generic.FormView):
    form_class = forms.UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home_view')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        if form.is_valid():
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('login_view')
            
        return super().form_valid(form)
    
    
    
class UserLoginForm(generic.FormView):
    form_class = forms.LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy("home_view")
    
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        if form.is_valid():
            user =  authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return redirect('home_view')
            else:
                return redirect("login_view")
        
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_view')