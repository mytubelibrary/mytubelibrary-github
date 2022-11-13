from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from base.forms import CategoriaForm
from base.models import Categoria


def agradecimentos(request):

	return render(request, 'base/agradecimentos.html')


class CategoriaIndexView(ListView):
	model = Categoria
	template_name = 'base/categoria-index.html'
	context_object_name = 'categoria_context'

	def get_queryset(self):

		if self.request.user.is_authenticated:

			return super().get_queryset().filter(categoria_usuario=self.request.user)

		else:
			return super().get_queryset().filter(categoria_usuario=None)


class CategoriaUpdateview(SuccessMessageMixin, UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'base/categoria-update.html'
	success_message = 'As alterações foram efectuadas com sucesso'

	def get_queryset(self):

		if self.request.user.is_authenticated:

			return super().get_queryset().filter(categoria_usuario=self.request.user)

		else:
			return super().get_queryset().filter(categoria_usuario=None)

	def get_success_url(self):

		return reverse('categoria-index')


class CategoriaDeleteView(DeleteView):
	model = Categoria
	template_name = 'base/categoria-delete.html'
	success_url = reverse_lazy('categoria-index')

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return super().get_queryset().filter(categoria_usuario=self.request.user)

		else:
			return super().get_queryset().filter(categoria_usuario=None)


class CategoriaFormView(CreateView):

	template_name = 'base/form-categoria.html'
	success_url = reverse_lazy('form-canal')

	def post(self, request, *args, **kwargs):
		form = CategoriaForm(request.POST)
		categoria_nome = request.POST.get('categoria_nome')
		usuario = self.request.user

		if 'btn_cadastro_categoria' in self.request.POST:

			if Categoria.objects.filter(categoria_usuario=usuario).filter(
					categoria_nome=categoria_nome).exists():

				messages.error(request, 'A categoria já existe')

				return redirect('form-canal')

		if form.is_valid():
			form_model = form.save(commit=False)
			form_model.categoria_usuario = self.request.user
			form_model.save()

			messages.success(request, 'Categoria adicionada com sucesso')
			return redirect('form-canal')


class CategoriaFormView2(CategoriaFormView):
	template_name = 'base/form-categoria2.html'
	success_url = reverse_lazy('categoria-index')

	def post(self, request, *args, **kwargs):
		form = CategoriaForm(request.POST)
		categoria_nome = request.POST.get('categoria_nome')
		usuario = self.request.user

		if 'btn_cadastro_categoria' in self.request.POST:

			if Categoria.objects.filter(categoria_usuario=usuario).filter(
					categoria_nome=categoria_nome).exists():

				messages.error(request, 'A categoria já existe')

				return redirect('categoria-index')

		if form.is_valid():
			form_model = form.save(commit=False)
			form_model.categoria_usuario = self.request.user
			form_model.save()

			messages.success(request, 'Categoria adicionada com sucesso')
			return redirect('categoria-index')


class CategoriaFormView3(CategoriaFormView):
	template_name = 'base/form-categoria3.html'
	success_url = reverse_lazy('form-playlist')

	def post(self, request, *args, **kwargs):
		form = CategoriaForm(request.POST)
		categoria_nome = request.POST.get('categoria_nome')
		usuario = self.request.user

		if 'btn_cadastro_categoria' in self.request.POST:

			if Categoria.objects.filter(categoria_usuario=usuario).filter(
					categoria_nome=categoria_nome).exists():

				messages.error(request, 'A categoria já existe')

				return redirect('form-playlist')

		if form.is_valid():
			form_model = form.save(commit=False)
			form_model.categoria_usuario = self.request.user
			form_model.save()

			messages.success(request, 'Categoria adicionada com sucesso')
			return redirect('form-playlist')
