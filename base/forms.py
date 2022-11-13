from django import forms

from base.models import Categoria


class CategoriaForm(forms.ModelForm):

	class Meta():
		model = Categoria
		fields = [
			'categoria_nome'
		]
