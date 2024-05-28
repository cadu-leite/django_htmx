from django.shortcuts import render

from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"

class HtmxClick(TemplateView):
    template_name = "htmx_click.html"

class HtmxOnLoad(TemplateView):
    template_name = "htmx_onload.html"

class HtmxClickOOB(TemplateView):
    template_name = "htmx_click_oob.html"
