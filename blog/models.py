from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField


class VideoGamePage(Page):
    description = RichTextField()
    cover = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    release_date = models.DateField()
    platforms = StreamField([
        ('platform', blocks.CharBlock(max_length=255)),
    ])
    genero = models.CharField(max_length=255, null=True, blank=True)
    desarrollador = models.CharField(max_length=255, null=True, blank=True)
    editor = models.CharField(max_length=255, null=True, blank=True)
    jugadores = models.CharField(max_length=255, null=True, blank=True)
    modosdejuego = models.CharField(max_length=255, null=True, blank=True)
    requisitos = models.CharField(max_length=255, null=True, blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('cover'),
        FieldPanel('release_date'),
        StreamFieldPanel('platforms'),
        FieldPanel('genero'),
        FieldPanel('desarrollador'),
        FieldPanel('editor'),
        FieldPanel('jugadores'),
        FieldPanel('modosdejuego'),
        FieldPanel('requisitos'),
    ]

    class listadojuegos(Page):
        def get_context(self, request):
            context = super().get_context(request)
            listadojuegos = self.get_children().live().order_by()
            context['listadojuegos'] = listadojuegos
            return context

