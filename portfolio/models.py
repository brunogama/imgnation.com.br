# -*- coding: utf-8 -*-

from django.db import models
from transmeta import TransMeta
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Categoria(models.Model):
	"""(TrabalhoCategory description)"""
	# __metaclass__ = TransMeta
	
	category_title = models.CharField(blank=True, max_length=100)
	creation_date = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ('creation_date',)
		# get_latest_by = ''
		verbose_name_plural = 'Categorias'
		# translate = ('app_name', 'app_description', 'app_url',)

	def __unicode__(self):
		return self.category_title


app_image_help_txt = u'As imagens não devem passar de 512px de largura por 420px de altura'


class Imagem(models.Model):
	"""(TrabalhoImage description)"""
	__metaclass__ = TransMeta
	
	image = models.ImageField(upload_to="uploads/")
	short_description = models.CharField(blank=True, max_length=100, verbose_name=u'Título')
	description = models.TextField(blank=True, verbose_name=u'Texto')
	creation_date = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		ordering = ('creation_date',)
		get_latest_by = 'creation_date'
		verbose_name_plural = 'Imagens'
		translate = ('short_description', 'description',)

	def __unicode__(self):
		return self.short_description


class Trabalho(models.Model):
	"""(Trabalho description)"""
	__metaclass__ = TransMeta
    
	name = models.CharField(blank=False, max_length=100, verbose_name=u'Trabalho')
	description = models.TextField(blank=False, verbose_name=u'Texto')
	url = models.URLField(blank=True, verify_exists=True, verbose_name=u'Site')
	images = models.ManyToManyField(Imagem, blank=True)
	category = models.ForeignKey(Categoria, verbose_name=u'Categoria')
	creation_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Data de Criação')
	slug = models.SlugField(max_length = 100, blank = True, unique=True, editable=False)
	
	class Meta:
		ordering = ('creation_date',)
		verbose_name_plural = 'Trabalhos'
		translate = ('name', 'description', 'url',)

	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('portfolio', args=[self.slug,])



def TrabalhoPreSave(signal, instance, sender, **kwargs):
	if instance.name_en:
		slug_string = instance.name_en
		instance.slug = slugify(slug_string)

signals.pre_save.connect(TrabalhoPreSave, sender=Trabalho)