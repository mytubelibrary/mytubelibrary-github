from django.urls import path
from playlists.views import (
	PlaylistIndexView,
	PlaylistBuscaView,
	PlaylistCategoriaIndexView,
	PlaylistDetailView,
	PlaylistUpdateView,
	PlaylistDeleteView,
	PlaylistFormView,
)


urlpatterns = [
	path('', PlaylistIndexView.as_view(), name='playlist-index'),
	path('busca/', PlaylistBuscaView.as_view(), name='playlist-busca'),
	path('playlist-categoria/<str:categoria>/', PlaylistCategoriaIndexView.as_view(), name='playlist-categoria'),
	path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
	path('form-playlist/', PlaylistFormView.as_view(), name='form-playlist'),
	path('<int:pk>/update/', PlaylistUpdateView.as_view(), name='playlist-update'),
	path('<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist-delete'),
]