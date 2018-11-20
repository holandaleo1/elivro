from .models import Category
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

#######Executando Consultas SQL personalizadas sem abstração##########


#######Consultas Relacionadas com o Category########

#Equivalente a "Category.objects.all()"     
def SELECT_ALL(table):
	objeto_all = []
	for categ in Category.objects.raw("SELECT * FROM "+table):
		objeto_all.append(categ)
	return objeto_all

#Equivalente a "category = Category.objects.get(slug=slug)" 

def SELECT_WHERE(*args,**kwargs):	
	for objt in Category.objects.raw("SELECT * FROM catalog_category WHERE slug =%s",[kwargs['slug']]):
		pass
	return objt

    

