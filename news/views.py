from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import News,Category,Ads,Vision,Mission,services,Member,Contact
from django.views import View
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context ['trending'] = News.objects.all().order_by('-views')[:3]
        context['right_trending'] = News.objects.all().order_by('-pub_date')[3:5]
        context['most_recent'] = News.objects.all().order_by()[8:13]
        context['most_popular']= News.objects.all().order_by()[12:16]
        context['corsel']= News.objects.all().order_by('-views')[4:9]
        context['categories'] = Category.objects.filter(display_in_home=True)
        context['ads'] = Ads.objects.all()


        context['news'] = {}
        for category in context['categories']:
            context['news'][category] = News.objects.filter(category = category)[:5]

        
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context['visions'] =Vision.objects.all().order_by('-created_at')[:5]
        context['missions'] = Mission.objects.all().order_by('-created_at')[:5]
        context['services'] = services.objects.all().order_by('-created_at')[:5]
        context['mebers'] = Member.objects.all()
        return context
    

class CategoryPageView(TemplateView):
    template_name = 'category.html'
    paginate_by = 6

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs) 
        context['categories'] = Category.objects.all()
        context['news'] = {}
        page_number = self.request.GET.get('page', 1) 
        for category in context['categories']:
           
            news_list= News.objects.filter(category = category)
            paginator = Paginator(news_list, self.paginate_by)
            
            try:
                news_page = paginator.page(page_number)
            except PageNotAnInteger:
                news_page = paginator.page(1)
            except EmptyPage:
                news_page = paginator.page(paginator.num_pages)
            context['news'][category] = news_page

        return context                                                                                                                                                                                                                               




class ContactUsPageView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        contact_table = Contact()
        contact_table.Sender = data.get("name")
        contact_table.sender_email = data.get("email")
        contact_table.subject = data.get("subject")
        contact_table.message = data.get("message")
        contact_table.save()

        subject = f'{contact_table.subject}'
        message = f"Name: {contact_table.Sender}\nEmail: {contact_table.sender_email}\nMessage: {contact_table.message}"
        from_email = '' # add system email
        recipient_list = []  #add recepient email
        send_mail(subject, message, from_email, recipient_list)
        
        messages.success(request, 'Message sent successfully!')
        return redirect("contactus")


class Description (View):
    def get(self, request, id):
        data = News.objects.get(id=id)
        data.views += 1
        data.save()

        return render(request,"description.html",{'news':data})

