from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class AboutPage(Page):
    template = "acercade/about_page.html"
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
