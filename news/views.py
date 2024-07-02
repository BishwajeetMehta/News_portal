from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import News,Category
from django.views import View

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context ['trending'] = News.objects.all().order_by('-views')[:3]
        context['right_trending'] = News.objects.all().order_by('-pub_date')[3:5]
        context['most_recent'] = News.objects.all().order_by()[8:11]
        context['most_popular']= News.objects.all().order_by()[12:16]
        
        context['corsel']= News.objects.all().order_by('-views')[4:9]
        context['categories'] = Category.objects.filter(display_in_home=True)
        
       

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


class Description (View):
    def get(self, request, id):
        data = News.objects.get(id=id)
        data.views += 1
        data.save()

        return render(request,"description.html",{'news':data})

