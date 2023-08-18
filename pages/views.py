# Schyler Lowry
# CIS-218
# 5/25/2023

from django.views.generic import TemplateView

import ast

import requests

"""Using the class method to render pages from the corresponding templates."""

class HomePageView(TemplateView):
    template_name = "home.html"

    

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #authtoken = self.request.GET.get("code")
        context["code"] = self.request.GET.get("code")
        return context

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class AnimeMainPageView(TemplateView):
    template_name = "anime_main.html"
    #something = requests.get("https://httpbin.org/status/200")

    header = {
        "X-MAL-CLIENT-ID": "5a0f93541f97d27dc90508a793000126"
    }

    #anime = requests.get("https://api.myanimelist.net/v2/anime/30230?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity", headers=header)
    anime = requests.get("https://api.myanimelist.net/v2/anime/ranking?ranking_type=all&limit=4", headers=header)
    anime_dict = anime.json()
    #anime_dict = ast.literal_eval(anime.text)
    
    print("My type is:", type(anime_dict))
    
    
    def get_context_data(self, **kwargs):
        context = super(AnimeMainPageView, self).get_context_data(**kwargs)
        context["anime"] = self.anime_dict
        return context
    

