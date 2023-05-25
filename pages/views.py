# Schyler Lowry
# CIS-218
# 5/25/2023

from django.views.generic import TemplateView

"""Using the class method to render pages from the corresponding templates."""

class HomePageView(TemplateView):
    template_name = "home.html"

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

