from django.urls import path
from .views import CancionListView, CancionDetailView

urlpatterns = [
    path('canciones/', CancionListView.as_view(), name='cancion-lista'),
    path('canciones/<int:pk>/', CancionDetailView.as_view(), name='cancion-detalle'),
]
