from wagtail.contrib.views import PagesDetailView
from .models import AboutPage

class AboutPageView(PagesDetailView):
    model = AboutPage
    template_name = 'about_page.html'
