from django import forms

from playlists.models import Playlist


class PlaylistCadastroForm(forms.ModelForm):

	class Meta():
		model = Playlist

		fields = [
			'playlist_nome',
			'playlist_canal',
			'playlist_categoria',
			'playlist_dia',
			'playlist_hora',
			'playlist_idioma',
			'playlist_numero_v',
			'playlist_observacoes',
			'playlist_url',
			'playlist_foto',
		]