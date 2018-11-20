from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls  import reverse


class Category(models.Model):

    name = models.CharField(_('Nome'), max_length=50)
    slug = models.SlugField(_('Identificador'), max_length=100)

    created = models.DateTimeField(_('Criado em'), auto_now_add=True)
    modified = models.DateTimeField(_('Modificado em'), auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class Product(models.Model):

    name = models.CharField(_('Nome'), max_length=100)
    slug = models.SlugField(_('Identificador'), max_length=100)
    category = models.ForeignKey('catalog.Category', on_delete = models.PROTECT ,verbose_name='Categoria')
    description = models.TextField(_('Descrição'), blank=True)
    price = models.DecimalField(_('Preço'), decimal_places=2, max_digits=8)
    created = models.DateTimeField(_('Criado em'), auto_now_add=True)
    modified = models.DateTimeField(_('Modificado em'), auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
    def __str__(self):
    	return self.name
    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})