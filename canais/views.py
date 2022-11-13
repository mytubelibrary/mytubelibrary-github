from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from canais.forms import CanalCadastroForm
from canais.models import Canal
from playlists.models import Playlist
from base.models import Categoria, DiaTransmissao


def error_404(request, exception):
	data = {}
	return render(request, 'canais/404.html', data)


class IndexView(ListView):
	model = Canal
	template_name = 'canais/index.html'
	paginate_by = 15
	context_object_name = 'canais_context'

	def get_queryset(self):

		if self.request.user.is_authenticated:

			cat = Categoria.objects.filter(categoria_usuario=self.request.user)
			dia = DiaTransmissao.objects.all()

			self.extra_context = {
				'categoria_context': cat,
	 			'dia_context': dia
			}

			return super().get_queryset().filter(canal_usuario=self.request.user)

		else:
			return super().get_queryset().filter(canal_usuario=None)


class CanalBuscaView(IndexView):
	template_name = 'canais/canais-busca.html'
	paginate_by = 0

	def get_queryset(self):
		qs = super().get_queryset()
		termo = self.request.GET.get('termo')

		if termo:

			qs = qs.filter(
				# Q(canal_nome__icontains=termo) |
				Q(canal_nome__istartswith=termo)
				# Q(canal_categoria__categoria_nome__icontains=termo) |
				# Q(canal_categoria__categoria_nome__startswith=termo)
			)

			return qs


class CanalCategoriaIndexView(IndexView):

	def get_queryset(self):

		qs = super().get_queryset()
		categoria = self.kwargs.get('categoria', None)

		qs = qs.filter(canal_categoria__categoria_nome__iexact=categoria)

		return qs


class CanalDiaIndexView(IndexView):

	def get_queryset(self):

		qs = super().get_queryset()
		dia = self.kwargs.get('dia', None)

		qs = qs.filter(canal_dia_trans__dia_transmissao__iexact=dia)

		return qs


class CanalDetailview(DetailView):
	model = Canal
	template_name = 'canais/canal-detail.html'
	context_object_name = 'canal'
	extra_context = ''

	def get_queryset(self):

		if self.request.user.is_authenticated:

			self.extra_context = {
				'canal_obj': Canal.objects.filter(canal_usuario=self.request.user),
				'playlist_obj': Playlist.objects.filter(
					playlist_usuario=self.request.user)
			}

			return super().get_queryset().filter(canal_usuario=self.request.user)

		else:
			return super().get_queryset().filter(canal_usuario=None)


class CanalUpdateView(SuccessMessageMixin, UpdateView):
	model = Canal
	form_class = CanalCadastroForm
	template_name = 'canais/canal-update.html'
	success_message = 'As alterações do seu canal foram efectuadas com sucesso'

	def get_form(self, form_class=None):

		can = Canal.objects.filter(canal_usuario=self.request.user)
		cat = Categoria.objects.filter(categoria_usuario=self.request.user)

		form = super(CanalUpdateView, self).get_form(form_class)
		form.fields["canal_idioma"].queryset = can
		form.fields["canal_categoria"].queryset = cat

		return form

	def get_queryset(self):

		if self.request.user.is_authenticated:

			return super().get_queryset().filter(canal_usuario=self.request.user)

		else:
			return super().get_queryset().filter(canal_usuario=None)

	def get_success_url(self):

		return reverse('canal-detail', kwargs={'pk': self.object.pk,})


class CanalDeleteView(DeleteView):
	model = Canal
	template_name = 'canais/canal-delete.html'
	success_url = reverse_lazy('index')

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return super().get_queryset().filter(canal_usuario=self.request.user)

		else:
			return super().get_queryset().filter(canal_usuario=None)


class CanalFormView(CreateView):
	template_name = 'canais/form-canal.html'
	success_url = reverse_lazy('form-canal')

	def get(self, request, *args, **kwargs):

		usuario = self.request.user
		form = CanalCadastroForm()

		if request.user.is_authenticated:

			cat = Categoria.objects.filter(categoria_usuario=usuario)
			form.fields['canal_categoria'].queryset = cat

		context = {'form': form}

		return render(request, 'canais/form-canal.html', context)

	def post(self, request, *args, **kwargs):

		form = CanalCadastroForm(request.POST, request.FILES)
		usuario = self.request.user
		canal_nome = request.POST.get('canal_nome')

		if 'btn_cadastro_canal' in self.request.POST:

			if Canal.objects.filter(canal_usuario=usuario).filter(
					canal_nome=canal_nome).exists():

				context = {'form': form}

				messages.error(request, 'O Canal não foi cadastrado por que já existe')
				return render(request, 'canais/form-canal.html', context)

			if form.is_valid():
				form_model = form.save(commit=False)
				form_model.canal_usuario = self.request.user
				form_model.save()
				form.save_m2m()

				messages.success(request, 'O Canal foi cadastrado com sucesso')
				return redirect('form-canal')

			else:
				messages.error(request, 'Erro ao cadastrar o canal')

				context = {'form': form}
				return render(request, 'canais/form-canal.html', context)
