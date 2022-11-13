from django.urls import path
from canais.views import (
	IndexView,
	CanalBuscaView,
	CanalCategoriaIndexView,
	CanalDiaIndexView,
	CanalFormView,
	CanalDetailview,
	CanalUpdateView,
	CanalDeleteView,
)

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('busca/', CanalBuscaView.as_view(), name='canal-busca'),
	path('canal-categoria/<str:categoria>', CanalCategoriaIndexView.as_view(), name='canal-categoria'),
	path('canal-dia/<str:dia>', CanalDiaIndexView.as_view(), name='canal-dia'),
	path('form-canal/', CanalFormView.as_view(), name='form-canal'),
	path('<int:pk>/', CanalDetailview.as_view(), name='canal-detail'),
	path('<int:pk>/update/', CanalUpdateView.as_view(), name='canal-update'),
	path('<int:pk>/delete/', CanalDeleteView.as_view(), name='canal-delete'),
]
