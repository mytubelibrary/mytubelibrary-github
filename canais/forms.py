from django import forms

from canais.models import Canal


class CanalCadastroForm(forms.ModelForm):

	class Meta():
		model = Canal

		fields = [
			'canal_nome',
			'canal_subtitulo',
			'canal_categoria',
			'canal_idioma',
			'canal_dia_trans',
			'canal_hora_trans',
			'canal_programas',
			'canal_observacoes',
			'canal_url',
			'canal_site',
			'canal_facebook',
			'canal_twitter',
			'canal_instagram',
			'canal_foto',
		]
