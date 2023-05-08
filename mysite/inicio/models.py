from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

class StreamerPage(Page):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    birth_city = models.CharField(max_length=255)
    birth_country = models.CharField(max_length=255)
    birth_coordinates = models.CharField(max_length=255)
    biography = models.TextField()
    social_links = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('full_name'),
        FieldPanel('date_of_birth'),
        FieldPanel('birth_city'),
        FieldPanel('birth_country'),
        FieldPanel('birth_coordinates'),
        FieldPanel('biography'),
        FieldPanel('social_links'),
    ]