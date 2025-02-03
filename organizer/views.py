from django.views.generic import ListView, DetailView
from .models import Cancion
import fitz 
from pathlib import Path

# Vista para listar todas las canciones
class CancionListView(ListView):
    model = Cancion
    template_name = 'canciones/lista_canciones.html'  # Ruta de la plantilla
    context_object_name = 'canciones'  # Nombre del objeto en el template

# Vista para ver los detalles de una canción
class CancionDetailView(DetailView):
    model = Cancion
    template_name = 'canciones/detalle_cancion.html'  # Ruta de la plantilla
    context_object_name = 'cancion'
    
    def get_context_data(self, **kwargs):
        # Obtener el contexto original
        context = super().get_context_data(**kwargs)

        # Obtener la canción actual
        cancion = self.get_object()

        # Filtrar las tablaturas relacionadas (por ejemplo, solo las que contienen "guitarra" en la descripción)
        tablaturas = cancion.tablaturas.all()

        # Agregar las tablaturas filtradas al contexto
        context['tablaturas'] = tablaturas

        return context