from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'uni/index.html'
