from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic

from main.forms import LibUserForm


def index(request):
    return render(request, 'pages/index.html')


class CreateCustomUserView(generic.FormView):
    template_name = 'pages/user_create.html'
    form_class = LibUserForm

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "User successfully created")
        return HttpResponseRedirect(reverse('main:home'))
