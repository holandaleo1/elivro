from .models import Category
from .sql_query import SELECT_ALL

#######Executando Consultas SQL personalizadas sem abstração##########
"""
#Equivalente a "Category.objects.all()"     
def SELECT_ALL(table):
	objeto_all = []
	for categ in Category.objects.raw("SELECT * FROM "+table):
		objeto_all.append(categ)
	return objeto_all"""


def categories(request):
    return {
        'categories': SELECT_ALL("catalog_category")
    }