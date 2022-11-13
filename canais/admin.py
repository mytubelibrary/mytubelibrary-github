from django.contrib import admin

from canais.models import Canal
from canais.forms import CanalCadastroForm


class CanalAdmin(admin.ModelAdmin):

	form = CanalCadastroForm

	list_display = [
		'canal_nome',
		'canal_subtitulo',
		'categoria',
		'canal_idioma',
		'dia_transmissao',
		'hora_transmissao'
	]

	def get_queryset(self, request):

		qs = super().get_queryset(request)
		return qs.filter(canal_usuario=request.user)

	def save_model(self, request, obj, form, change):
		obj.canal_usuario = request.user
		super().save_model(request, obj, form, change)


admin.site.register(Canal, CanalAdmin)
