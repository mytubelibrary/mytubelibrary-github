from django.db import models

from django.contrib.auth import get_user_model


class Categoria(models.Model):
	categoria_usuario = models.ForeignKey(get_user_model(), verbose_name='Usuário',
									  on_delete=models.CASCADE)
	categoria_nome = models.CharField('Categoria', max_length=30)

	class Meta():
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['categoria_nome']

	def __str__(self):
		return self.categoria_nome


class DiaTransmissao(models.Model):
	dia_transmissao = models.CharField('Dias de Transmissão', max_length=50)

	class Meta():
		verbose_name = 'Dia de transmissão'
		verbose_name_plural = 'Dias de transmissão'
		ordering = ['id']

	def __str__(self):
		return self.dia_transmissao


class HoraTransmissao(models.Model):
	hora_transmissao = models.CharField('Hora de transmissão', max_length=10)

	class Meta():
		verbose_name = 'Hora de transmissão'
		verbose_name_plural = 'Horas de transmissão'
		ordering = ['hora_transmissao']

	def __str__(self):
		return self.hora_transmissao
