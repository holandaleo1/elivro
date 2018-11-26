"""djangoEcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.urls import path
from core.views import *
#from django.contrib.auth import authenticate, login
#from django.contrib.auth.views import LoginView
#from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views


from catalog import views as views_catalog

urlpatterns = [
	url(r'^$', index,name='index'),
	url('contato/', contact,name='contact'),
    url(r'^entrar/$',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^sair/$', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
	#url('produtos/',product_list,name='product_list'),
    #url(r'^registro/$',register, name='register'),
	url(r'^catalogo/', include('catalog.urls')),
    url(r'^conta/', include('accounts.urls')),
    url(r'^compras/', include('checkout.urls')),
	#url('produto/', product,name='product'),
    path('admin/', admin.site.urls),
]
