from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import News

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context ['trending'] = News.objects.all().order_by()[:3]
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

class CategoryPageView(TemplateView):
    template_name = 'category.html'


class LatestNewsPageView(TemplateView):
    template_name = 'latest_news.html'

class ContactUsPageView(TemplateView):
    template_name = 'contact.html'

