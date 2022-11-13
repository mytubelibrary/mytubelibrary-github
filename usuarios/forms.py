from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from usuarios.models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):

	class Meta():
		model = CustomUsuario
		fields = ('first_name', 'last_name', 'username')
		labels = {'username': 'Username/Email'}

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data["username"]

		if commit:
			user.save()

		return user


class CustomUsuarioChangeForm(UserChangeForm):

	class Meta():
		model = CustomUsuario
		fields = ('first_name', 'last_name', 'email')

	def save(self, commit=True):
		user = super().save(commit=False)
		user.username = self.cleaned_data["email"]

		if commit:
			user.save()

		return user
