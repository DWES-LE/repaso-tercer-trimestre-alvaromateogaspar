from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.db.models import CharField

class AboutPage(Page):
    template = "acercade/about_page.html"
    body = CharField(max_length=8000, null=True, blank=True)
    
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
