from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import News,Category

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context ['trending'] = News.objects.all().order_by()[:3]
        context['right_trending'] = News.objects.all().order_by()[1:3]
        context['categories'] = Category.objects.all()[:5]
        context['news'] = {}
        for category in context['categories']:
            context['news'][category] = News.objects.filter(category = category)[:5]

        
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

class CategoryPageView(TemplateView):
    template_name = 'category.html'


class LatestNewsPageView(TemplateView):
    template_name = 'latest_news.html'

class ContactUsPageView(TemplateView):
    template_name = 'contact.html'

