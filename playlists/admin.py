from django.contrib import admin

from playlists.models import Playlist


class PlaylistAdmin(admin.ModelAdmin):

	list_display = (
		'playlist_nome',
		'playlist_canal',
		'categoria',
		'playlist_idioma',
		'playlist_numero_v'
	)

	exclude = ['playlist_usuario']

	def get_queryset(self, request):

		qs = super().get_queryset(request)
		return qs.filter(playlist_usuario=request.user)

	def save_model(self, request, obj, form, change):

		obj.playlist_usuario = request.user
		super().save_model(request, obj, form, change)


admin.site.register(Playlist, PlaylistAdmin)
