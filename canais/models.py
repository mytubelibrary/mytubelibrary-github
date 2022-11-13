from django.db import models

from base.models import Categoria, DiaTransmissao, HoraTransmissao
from django.contrib.auth import get_user_model


def upload_to(instance, filename):
	return 'canal_img/{}/{}'.format(
		instance.canal_usuario.id, filename)


class Canal(models.Model):
	idioma_choices = [
		('Português', 'Português'),
		('Inglês', 'Inglês'),
		('Espanhol', 'Espanhol'),
		('Italiano', 'Italiano'),
		('Francês', 'Francês'),
		('Alemão', 'Alemão'),
	]

	canal_usuario = models.ForeignKey(get_user_model(), verbose_name='Usuário',
									  on_delete=models.CASCADE)
	canal_nome = models.CharField('Canal', max_length=30)
	canal_subtitulo = models.CharField('Subtitulo', max_length=50, blank=True)
	canal_categoria = models.ManyToManyField(Categoria)
	canal_idioma = models.CharField('Idioma', max_length=20,
									choices=idioma_choices,
									default='Português')
	canal_dia_trans = models.ManyToManyField(DiaTransmissao, blank=True)
	canal_hora_trans = models.ManyToManyField(HoraTransmissao, blank=True)
	canal_programas = models.TextField('Programas', blank=True, max_length=500)
	canal_observacoes = models.TextField('Observações', blank=True,
										 max_length=1500)
	canal_url = models.URLField('Link', max_length=300)
	canal_site = models.URLField('Site', max_length=300, blank=True)
	canal_facebook = models.URLField('Facebook', max_length=300, blank=True)
	canal_twitter = models.URLField('Twitter', max_length=300, blank=True)
	canal_instagram = models.URLField('Instagram', max_length=300, blank=True)
	canal_foto = models.ImageField(upload_to=upload_to)

	def categoria(self):
		return ', '.join([str(p) for p in self.canal_categoria.all()])

	def dia_transmissao(self):
		return ', '.join([str(p) for p in self.canal_dia_trans.all()])

	def hora_transmissao(self):
		return ', '.join([str(p) for p in self.canal_hora_trans.all()])

	class Meta():
		verbose_name = 'Canal'
		verbose_name_plural = 'Canais'
		ordering = ['canal_nome']

	def __str__(self):
		return self.canal_nome
