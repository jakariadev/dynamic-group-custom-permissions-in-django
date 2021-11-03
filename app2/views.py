from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


class HomePageView2(TemplateView):
    template_name = 'home2.html'


class AboutPageView2(TemplateView):
    template_name = 'about2.html'
