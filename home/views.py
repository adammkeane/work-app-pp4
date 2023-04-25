from django.shortcuts import render
from django.views import generic, View


class HomePage(generic.TemplateView):
    """View to show the home page"""
    template_name = 'home/index.html'
