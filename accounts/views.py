
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView, FormMixin
)
from django.views.generic import (
    TemplateView, DetailView, View
)
from django.urls import reverse_lazy
from accounts.models import (
    User, 
)
from .forms import (
    NewUserForm, UpdateUserForm, 
)
from django.contrib.auth import authenticate, login
from .tasks import welcome_user



class RegisterUser(CreateView):
    model = User
    form_class = NewUserForm
    template_name = 'accounts/forms/registration_form.html'
    success_url = '/accounts/profile'
    
    def form_valid(self, form):
        new_user = form.save()
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        welcome_user.delay(new_user.id)
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)    

# @login_required(login_url='/accounts/login')
def profile(request):
    if request.user.is_superuser:
        return redirect('dashboard:index')
    else:
        return redirect('home:index')
    
        
 
class UserChangeView(LoginRequiredMixin, UpdateView):
    login_url ='/accounts/login'
    model = User
    # fields = ['email', 'tel_no', 'instagram_handle', 'country', 'location']
    form_class = UpdateUserForm
    template_name = 'accounts/forms/user_change_form.html'
    
    def get_success_url(self):
        return reverse_lazy('accounts:profile')

class UpdateUserView(LoginRequiredMixin, UpdateView):
    login_url= '/accounts/login'
    model = User
    form_class = UpdateUserForm
    template_name = 'accounts/forms/user_update_form.html'

    
    def get_success_url(self):
        return reverse_lazy('accounts:profile')


def custom_forbidden(request, exception=None):
    return render(request, 'accounts/forbidden.html', status=403)


def page_not_found(request, exception=None):
    return render(request, 'accounts/page_not_found.html', status=404)

def server_error(request, exception=None):
    return render(request, 'accounts/server_error.html', status=500)


def bad_request(request, exception=None):
    return render(request, 'accounts/bad_request.html', status=400)

