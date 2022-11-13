from django.urls import path
from base.views import (
	CategoriaIndexView,
	CategoriaFormView,
	CategoriaFormView2,
	CategoriaFormView3,
	CategoriaUpdateview,
	CategoriaDeleteView,
	agradecimentos,
)


urlpatterns = [
	path('categoria-index/', CategoriaIndexView.as_view(), name='categoria-index'),
	path('form-categoria/', CategoriaFormView.as_view(), name='form-categoria'),
	path('form-categoria2/', CategoriaFormView2.as_view(), name='form-categoria2'),
	path('form-categoria3/', CategoriaFormView3.as_view(), name='form-categoria3'),
	path('<int:pk>/update/', CategoriaUpdateview.as_view(), name='categoria-update'),
	path('<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria-delete'),
	path('agradecimentos/', agradecimentos, name='agradecimentos'),
]