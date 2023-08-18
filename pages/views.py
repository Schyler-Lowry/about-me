# Schyler Lowry
# CIS-218
# 5/25/2023

from django.views.generic import TemplateView

import requests

"""Using the class method to render pages from the corresponding templates."""

class HomePageView(TemplateView):
    template_name = "home.html"

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class AnimeMainPageView(TemplateView):
    template_name = "anime_main.html"
    something = requests.get("https://httpbin.org/status/200")
    
    def get_context_data(self, **kwargs):
        context = super(AnimeMainPageView, self).get_context_data(**kwargs)
        context["something"] = self.something
        return context
    

