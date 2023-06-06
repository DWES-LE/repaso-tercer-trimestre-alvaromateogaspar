from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index




# Keep the definition of BlogIndexPage, and add:


class BlogPage(Page):
    nombre = models.CharField(max_length=255)
    date = models.DateField("Fecha de nacimiento")
    lugar_de_nacimiento = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)
    enlace_redes_sociales = models.CharField(max_length=200)
    otros_detalles = models.CharField(max_length=1000)

    
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('nombre'),
        index.SearchField('lugar_de_nacimiento'),
        index.SearchField('body'),
        index.SearchField('enlace_redes_sociales'),
        index.SearchField('otros_detalles'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('date'),
        FieldPanel('lugar_de_nacimiento'),
        FieldPanel('body'),
        FieldPanel('enlace_redes_sociales'),
        FieldPanel('otros_detalles'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    class BlogPageGalleryImage(Orderable) :
        page = ParentalKey(Page ,on_delete=models.CASCADE, related_name='gallery_images')
        image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]