from django.contrib import admin
from .models import Cancion, Tablatura, LinkVideo, Grabacion, Ensayo, GrabacionEnsayo, Evento, MultimediaEvento, Compras

class TablaturaInline(admin.TabularInline):
    model = Tablatura
    extra = 1  # Número de formularios vacíos para agregar tablaturas

class LinkVideoInline(admin.TabularInline):
    model = LinkVideo
    extra = 1  # Número de formularios vacíos para agregar links de video

class GrabacionInline(admin.TabularInline):
    model = Grabacion
    extra = 1  # Número de formularios vacíos para agregar grabaciones

class GrabacionEnsayoInline(admin.TabularInline):
    model = GrabacionEnsayo
    extra = 1  # Número de formularios vacíos para agregar grabaciones de ensayos

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nombre_banda', 'genero')
    search_fields = ('titulo', 'nombre_banda')
    list_filter = ('genero',)
    inlines = [TablaturaInline, LinkVideoInline, GrabacionInline]  # Agregar los inlines

@admin.register(Tablatura)
class TablaturaAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'archivo')
    search_fields = ('cancion__titulo',)

@admin.register(LinkVideo)
class LinkVideoAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'url')
    search_fields = ('cancion__titulo',)

@admin.register(Grabacion)
class GrabacionAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'archivo')
    search_fields = ('cancion__titulo',)

@admin.register(Ensayo)
class EnsayoAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'fecha', 'observacion')
    search_fields = ('cancion__titulo',)
    list_filter = ('fecha',)
    inlines = [GrabacionEnsayoInline]  # Agregar el inline para grabaciones de ensayos

@admin.register(GrabacionEnsayo)
class GrabacionEnsayoAdmin(admin.ModelAdmin):
    list_display = ('ensayo', 'archivo')
    search_fields = ('ensayo__cancion__titulo',)
    
class MultimediaEventoInline(admin.TabularInline):
    model = MultimediaEvento
    extra = 1  # Número de formularios vacíos para agregar multimedia

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'descripcion')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha',)
    inlines = [MultimediaEventoInline]  # Agregar el inline para multimedia

@admin.register(MultimediaEvento)
class MultimediaEventoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'tipo', 'archivo')
    search_fields = ('evento__titulo',)
    list_filter = ('tipo',)

@admin.register(Compras)
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'precio', 'completado')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('completado', 'autor')