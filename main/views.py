from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic

from main.forms import LibUserForm
from main.models import LibUser


def index(request):
    return render(request, 'pages/index.html')


class CreateCustomUserView(generic.FormView):
    template_name = 'pages/user_create.html'
    form_class = LibUserForm

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "User successfully created")
        return HttpResponseRedirect(reverse('main:users'))


class UpdateCustomUserView(generic.UpdateView):
    template_name = 'pages/user_update.html'
    form_class = LibUserForm
    model = LibUser

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(reverse('main:users'))


def user_list(request):
    user_list = LibUser.objects.all()
    context = {
        "user_list": user_list
    }
    return render(request, 'pages/lib_users.html', context)