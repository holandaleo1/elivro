from .models import Category
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.db import connection, transaction

#######Executando Consultas SQL personalizadas sem abstração##########


#######Consultas Relacionadas com o Category########

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


#Equivalente a "Category.objects.all()"     
def SELECT_ALL(table):
	"""
	results = []
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM "+table)
	row = dictfetchall(cursor)
	
	for i in range (len(row)):
		results.append(row[i]['name'])
	print("results",results)"""
	###sem alteração	
	objeto_all = []
	for categ in Category.objects.raw("SELECT * FROM "+table):
		objeto_all.append(categ)
	print("obejtoAll",objeto_all)
	return objeto_all

#Equivalente a "category = Category.objects.get(slug=slug)" 

def SELECT_WHERE(*args,**kwargs):	
	for objt in Category.objects.raw("SELECT * FROM {} WHERE slug ='{}'".format(kwargs['table'],kwargs['slug'])):
		pass
	return objt

def SELECT_1N_PRODUCT (**args):
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM catalog_category as cat,catalog_product as prod where cat.slug ='ac' and prod.category_id = cat.id")
	row = dictfetchall(cursor)
	

	
"""
def SELECT_GROUPBY(*args,**kwargs){
	for objt in Category.objects.raw("SELECT * FROM catalog_product WHERE slug =%s",[kwargs['slug']]):
		pass
	return objt
	
}"""

    

