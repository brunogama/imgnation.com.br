from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^portfolio/(?P<slug>[\w_-]+)/$', 'imgnation.portfolio.views.trabalhos', name='portfolio'),
	url(r'^games/$', 'imgnation.portfolio.views.games', name='games'),
	url(r'^apps/$', 'imgnation.portfolio.views.apps', name='apps'),
	url(r'^contact/$', 'imgnation.contato.views.contato', name='contato'),
	url(r'^contact/thank-you/$', 'imgnation.contato.views.contato_enviado', name='contato_enviado'),
	
	# url(r'^contato/obrigado/$', 'nossoalmoco.Contato.views.contato_enviado'),

)

	
urlpatterns += patterns('django.views.generic.simple',
	url(r'^$', 'direct_to_template', { 'template' : 'pages/home.html'}, name='home'),
	url(r'^blog/$', 'direct_to_template',{ 'template' : 'pages/blog.html'}, name='blog'),
	url(r'^about/$', 'direct_to_template', { 'template' : 'pages/about.html'}, name='about'),

	# url(r'^contact/thank-you/$', 'direct_to_template', { 'template' : 'pages/contact_sent.html'}, name='contact_sent'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^404/$', 'django.views.generic.simple.direct_to_template', { 'template' : '404.html'}, name='404'),
	)
		


# admin stuff
urlpatterns += patterns('',
	(r'^i18n/', include('django.conf.urls.i18n')),
	(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/filebrowser/', include('filebrowser.urls')),
	url(r'^admin_tools/', include('admin_tools.urls')),
)


if 'rosetta' in settings.INSTALLED_APPS:
	urlpatterns += patterns('',
		url(r'^rosetta/', include('rosetta.urls')),
	)