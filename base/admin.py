from django.contrib import admin

from base.models import Categoria, DiaTransmissao, HoraTransmissao


class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('categoria_nome',)
	exclude = ['categoria_usuario']

	def get_queryset(self, request):

		qs = super().get_queryset(request)
		return qs.filter(categoria_usuario=request.user)

	def save_model(self, request, obj, form, change):

		obj.categoria_usuario = request.user
		super().save_model(request, obj, form, change)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(DiaTransmissao)
admin.site.register(HoraTransmissao)