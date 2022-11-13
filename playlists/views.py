from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from playlists.models import Playlist
from playlists.forms import PlaylistCadastroForm
from base.models import Categoria
from canais.models import Canal


class PlaylistIndexView(SuccessMessageMixin, ListView):
	model = Playlist
	template_name = 'playlists/playlist-index.html'
	paginate_by = 15
	context_object_name = 'playlists_context'

	def get_queryset(self):

		if self.request.user.is_authenticated:

			cat = Categoria.objects.filter(categoria_usuario=self.request.user)

			self.extra_context = {
				'categoria_context': cat
			}

			return super().get_queryset().filter(playlist_usuario=self.request.user)

		else:
			return super().get_queryset().filter(playlist_usuario=None)


class PlaylistBuscaView(PlaylistIndexView):
	template_name = 'playlists/playlist-busca.html'
	paginate_by = 0

	def get_queryset(self):
		qs = super().get_queryset()
		termo = self.request.GET.get('termo')

		if termo:
			qs = qs.filter(
				# Q(canal_nome__icontains=termo) |
				Q(playlist_nome__istartswith=termo)
				# Q(canal_categoria__categoria_nome__icontains=termo) |
				# Q(canal_categoria__categoria_nome__startswith=termo)
			)

			return qs


class PlaylistCategoriaIndexView(PlaylistIndexView):

	def get_queryset(self):

		qs = super().get_queryset()
		categoria = self.kwargs.get('categoria', None)

		qs = qs.filter(playlist_categoria__categoria_nome__iexact=categoria)

		return qs


class PlaylistDetailView(DetailView):
	model = Playlist
	template_name = 'playlists/playlist-detail.html'
	context_object_name = 'playlist'
	extra_context = ''

	def get_queryset(self):

		if self.request.user.is_authenticated:

			self.extra_context = {
				'playlist_obj': Playlist.objects.filter(playlist_usuario=self.request.user),
				'canal_obj': Canal.objects.filter(canal_usuario=self.request.user)
			}

			return super().get_queryset().filter(playlist_usuario=self.request.user)

		else:
			return super().get_queryset().filter(playlist_usuario=None)


class PlaylistUpdateView(SuccessMessageMixin, UpdateView):
	model = Playlist
	form_class = PlaylistCadastroForm
	template_name = 'playlists/playlist-update.html'
	success_message = 'As alterações da sua playlist foram efectuadas com sucesso'

	def get_form(self, form_class=None):

		play = Playlist.objects.filter(playlist_usuario=self.request.user)
		cat = Categoria.objects.filter(categoria_usuario=self.request.user)

		form = super(PlaylistUpdateView, self).get_form(form_class)
		form.fields["playlist_idioma"].queryset = play
		form.fields["playlist_categoria"].queryset = cat

		return form

	def get_queryset(self):

		if self.request.user.is_authenticated:

			return super().get_queryset().filter(
				playlist_usuario=self.request.user)

		else:
			return super().get_queryset().filter(playlist_usuario=None)

	def get_success_url(self):

		return reverse('playlist-detail', kwargs={'pk': self.object.pk, })


class PlaylistDeleteView(DeleteView):
	model = Playlist
	template_name = 'playlists/playlist-delete.html'
	success_url = reverse_lazy('playlist-index')

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return super().get_queryset().filter(
				playlist_usuario=self.request.user)

		else:
			return super().get_queryset().filter(playlist_usuario=None)


class PlaylistFormView(CreateView):
	template_name = 'playlists/form-playlist.html'
	success_url = reverse_lazy('form-playlist')

	def get(self, request, *args, **kwargs):

		usuario = self.request.user
		form = PlaylistCadastroForm()

		if request.user.is_authenticated:
			cat = Categoria.objects.filter(categoria_usuario=usuario)
			form.fields['playlist_categoria'].queryset = cat

		context = {'form': form}

		return render(request, 'playlists/form-playlist.html', context)

	def post(self, request, *args, **kwargs):

		form = PlaylistCadastroForm(request.POST, request.FILES)
		usuario = self.request.user
		playlist_nome = request.POST.get('playlist_nome')

		if 'btn_cadastro_playlist' in self.request.POST:

			if Playlist.objects.filter(playlist_usuario=usuario).filter(
					playlist_nome=playlist_nome).exists():

				context = {'form': form}

				messages.error(request,
							   'A playlist não foi cadastrada por que já existe')

				return render(request, 'playlists/form-playlist.html', context)

			if form.is_valid():
				form_model = form.save(commit=False)
				form_model.playlist_usuario = self.request.user
				form_model.save()
				form.save_m2m()

				messages.success(request, 'A playlist foi cadastrada com sucesso')
				return redirect('form-playlist')

			else:
				messages.error(request, 'Erro ao cadastrar a playlist')

				context = {'form': form}
				return render(request, 'playlists/form-playlist.html', context)
