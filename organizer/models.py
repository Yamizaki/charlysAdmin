from django.db import models
from django.contrib.auth.models import User

class Cancion(models.Model):
    # Opciones para el campo de género musical
    GENEROS_MUSICALES = [
        ('ROCK', 'Rock'),
        ('POP', 'Pop'),
        ('CUMBIA', 'Cumbia'),
        ('BALADA', 'Balada'),
        ('OTRO', 'Otro'),
    ]

    # Campos del modelo
    titulo = models.CharField(max_length=200, verbose_name="Título de la canción")
    nombre_banda = models.CharField(max_length=200, verbose_name="Nombre de la banda")
    genero = models.CharField(max_length=50, choices=GENEROS_MUSICALES, verbose_name="Género musical")
    letra = models.FileField(upload_to='letras/', verbose_name="Archivo de letra", blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.nombre_banda}"

    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"


class Tablatura(models.Model):
    cancion = models.ForeignKey(Cancion, related_name='tablaturas', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='tablaturas/', verbose_name="Archivo de tablatura")

    def __str__(self):
        return f"Tablatura de {self.cancion.titulo}"


class LinkVideo(models.Model):
    cancion = models.ForeignKey(Cancion, related_name='links_video', on_delete=models.CASCADE)
    url = models.URLField(verbose_name="Link de video de referencia")

    def __str__(self):
        return f"Link de video de {self.cancion.titulo}"


class Grabacion(models.Model):
    cancion = models.ForeignKey(Cancion, related_name='grabaciones', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='grabaciones/', verbose_name="Archivo de grabación (audio/video)")

    def __str__(self):
        return f"Grabación de {self.cancion.titulo}"


class Ensayo(models.Model):
    cancion = models.ForeignKey(Cancion, related_name='ensayos', on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha del ensayo")
    observacion = models.TextField(verbose_name="Observación", blank=True, null=True)

    def __str__(self):
        return f"Ensayo de {self.cancion.titulo} - {self.fecha}"

    class Meta:
        verbose_name = "Ensayo"
        verbose_name_plural = "Ensayos"


class GrabacionEnsayo(models.Model):
    ensayo = models.ForeignKey(Ensayo, related_name='grabaciones', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='ensayos/grabaciones/', verbose_name="Archivo de grabación (audio/video)")

    def __str__(self):
        return f"Grabación de {self.ensayo.cancion.titulo} - {self.ensayo.fecha}"

class Evento(models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length=200, verbose_name="Título del evento")
    descripcion = models.TextField(verbose_name="Descripción del evento")
    observaciones = models.TextField(verbose_name="Observaciones", blank=True, null=True)
    fecha = models.DateField(verbose_name="Fecha del evento")

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class MultimediaEvento(models.Model):
    # Tipos de multimedia
    TIPO_MULTIMEDIA = [
        ('IMAGEN', 'Imagen'),
        ('VIDEO', 'Video'),
        ('AUDIO', 'Audio'),
    ]

    evento = models.ForeignKey(Evento, related_name='multimedia', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='eventos/multimedia/', verbose_name="Archivo multimedia")
    tipo = models.CharField(max_length=10, choices=TIPO_MULTIMEDIA, verbose_name="Tipo de multimedia")

    def __str__(self):
        return f"Multimedia de {self.evento.titulo} - {self.tipo}"
    
    
class Compras(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título de la compra")
    descripcion = models.TextField(verbose_name="Descripción de la compra")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    completado = models.BooleanField(default=False, verbose_name="Completado")
    autor = models.ForeignKey(User, related_name='compras', on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"