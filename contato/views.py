# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


from annoying.decorators import render_to


class FormContato(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	name = forms.CharField(max_length=100, required=True, label=_('Nome'))
	email = forms.EmailField(required=True, label=_('E-mail'))
	message = forms.Field(widget=forms.Textarea, required=True, label=_('Mensagem'))

	def enviar(self):
		e_name = '%(name)s' % self.cleaned_data
		e_email = '%(email)s' % self.cleaned_data
		from_email = '%s <%s>' % (e_name, e_email)

		# email_server = 'site@imgnation.com.br'
		subject = 'Mensagem enviada pelo site'
		message = u'''Nome: %(name)s
					Email: %(email)s
					Mensagem: %(message)s
					''' % self.cleaned_data

		message = message.replace('\t','')

		send_mail(subject, message, from_email ,['contato@imgnation.com.br'], fail_silently=False)


@render_to('pages/contact.html')
def contato(request):
	pars = {}
	if request.method == 'POST':
		form = FormContato(request.POST)
		if form.is_valid():
			try:
				form.enviar()

			except BadHeaderError:
				return HttpResponse('Invalid header found.')

			return HttpResponseRedirect(reverse('imgnation.contato.views.contato_enviado'))
	else:
		form = FormContato()

	pars['form'] = form
	return { 'pars' : pars }

@render_to('pages/contact_sent.html')
def contato_enviado(request):
	pars = {}
	pars['mostrar'] = 'Sua mensagem foi enviada com sucesso.'

	return { 'pars' : pars }