from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from usuarios.forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from usuarios.models import CustomUsuario
from django.contrib.auth.views import (
	PasswordChangeView,
	PasswordResetView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
)


class UsuarioCreate(SuccessMessageMixin, CreateView):
	model = CustomUsuario
	form_class = CustomUsuarioCreateForm
	template_name = 'usuarios/novo-usuario.html'
	success_url = reverse_lazy('index')
	success_message = 'Bem vindo! Faça login para começar a criar a sua biblioteca'


class UsuarioChange(SuccessMessageMixin, UpdateView):
	model = CustomUsuario
	form_class = CustomUsuarioChangeForm
	success_url = reverse_lazy('index')
	success_message = 'Alteração dos seus dados efetuada com sucesso'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class UsuarioDelete(DeleteView):
	model = CustomUsuario
	success_url = reverse_lazy('index')
	template_name = 'usuarios/usuario-delete.html'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
	template_name = 'usuarios/change-password.html'
	success_url = reverse_lazy('index')
	success_message = 'Alteração da senha efectuada com sucesso'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
	template_name = 'usuarios/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
	success_message = 'Sua senha foi redefenida corretamente, faça login para começar'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
	template_name = 'registration/login.html'
	success_message = 'Sua senha foi redefenida corretamente, faça login para começar'
