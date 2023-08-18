# Schyler Lowry
# CIS-218
# 5/25/2023

from django.urls import path

from .views import HomePageView, ProjectsPageView, ContactPageView, AnimeMainPageView

urlpatterns = [
    path("anime/", AnimeMainPageView.as_view(), name="anime"),
    path("projects/", ProjectsPageView.as_view(), name="projects"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("", HomePageView.as_view(), name="home"),
]