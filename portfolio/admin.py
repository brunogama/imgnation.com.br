# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Categoria, Imagem, Trabalho

class TrabalhoAdmin(admin.ModelAdmin):
	list_display = ('name','description','category',)
	list_filter = ('category', 'creation_date',)


admin.site.register(Trabalho, TrabalhoAdmin)
admin.site.register(Imagem)
admin.site.register(Categoria)