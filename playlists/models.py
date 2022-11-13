from django.db import models
from base.models import Categoria, DiaTransmissao, HoraTransmissao
from django.contrib.auth import get_user_model


def upload_to(instance, filename):
	return 'playlist_img/{}/{}'.format(
		instance.playlist_usuario.id, filename)


class Playlist(models.Model):
	idioma_choices = [
		('Português', 'Português'),
		('Inglês', 'Inglês'),
		('Espanhol', 'Espanhol'),
		('Italiano', 'Italiano'),
		('Francês', 'Francês'),
		('Alemão', 'Alemão'),
	]

	playlist_usuario = models.ForeignKey(get_user_model(), verbose_name='Usuário',
									  on_delete=models.CASCADE)
	playlist_nome = models.CharField('PlayList', max_length=100)
	playlist_canal = models.CharField('Canal', max_length=100, blank=True)
	playlist_categoria = models.ManyToManyField(Categoria)
	playlist_dia = models.ManyToManyField(DiaTransmissao, blank=True)
	playlist_hora = models.ManyToManyField(HoraTransmissao, blank=True)
	playlist_idioma = models.CharField('Idioma', max_length=30,
									   choices=idioma_choices,
									   default='Português')
	playlist_numero_v = models.CharField('Número de Vídeos',
										 blank=True, max_length=4)
	playlist_observacoes = models.TextField('Observações', blank=True,
										 max_length=1000)
	playlist_url = models.URLField('Link', max_length=300)
	playlist_foto = models.ImageField(upload_to=upload_to)

	def categoria(self):  # permite ManyToMany no display_field no Admin

		return ", ".join([str(p) for p in self.playlist_categoria.all()])

	def dia_transmissao(self):
		return ', '.join([str(p) for p in self.playlist_dia.all()])

	def hora_transmissao(self):
		return ', '.join([str(p) for p in self.playlist_hora.all()])

	class Meta():
		verbose_name = 'PlayList'
		verbose_name_plural = 'PlayLists'
		ordering = ['playlist_nome']

	def __str__(self):
		return self.playlist_nome
