#
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from .forms import ContactForm
from django.contrib.auth import get_user_model
from django.urls import reverse,reverse_lazy
User = get_user_model()

class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')
register = RegisterView.as_view()

"""
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)"""
"""
def contact(request):
	return render(request,'contact.html')"""
"""Removido
def product_list(request):
	return render(request,'product_list.html')
"""
"""
def product(request):
	return render(request,'product.html')"""
