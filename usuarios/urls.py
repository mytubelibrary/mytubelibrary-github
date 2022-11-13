from django.contrib import admin
from django.urls import path, include
from usuarios.views import (
	UsuarioCreate,
	UsuarioChange,
	PasswordChange,
	PasswordReset,
	PasswordResetConfirm,
	PasswordResetComplete,
	UsuarioDelete,
)

from django.contrib.auth.views import (
	PasswordResetDoneView,
)

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('novo-usuario/', UsuarioCreate.as_view(), name='novo-usuario'),
	path('<int:pk>/update/', UsuarioChange.as_view(), name='alteracao-dados'),
	path('change-password/', PasswordChange.as_view(), name='change-password'),
	path('password-reset/', PasswordReset.as_view(), name='password-reset'),
	path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name="password_reset_confirm"),
	path('login/', PasswordResetComplete.as_view(), name='password_reset_complete'),
	path('<int:pk>/delete/', UsuarioDelete.as_view(), name='usuario-delete'),
]
