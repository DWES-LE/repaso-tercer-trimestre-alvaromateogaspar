from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField

class Personajes(Page):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=255, null=True, blank=True)
    videojuego = models.CharField(max_length=255, null=True, blank=True)
    peso = models.CharField(max_length=255, null=True, blank=True)
    altura = models.CharField(max_length=255, null=True, blank=True)
    hijos = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('foto'),
        FieldPanel('fecha_nacimiento'),
        FieldPanel('lugar_nacimiento'),
        FieldPanel('videojuego'),
        FieldPanel('peso'),
        FieldPanel('altura'),
        FieldPanel('hijos'),
    ]

