from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel


@register_snippet
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    ciudad = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    #jugadores = models.ManyToManyField('Jugador')

    def __str__(self):
        return self.nombre

@register_snippet
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=100)
    equipo_actual = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    def __str__(self):
        return self.nombre
    
class PaginaDeEquipos(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

