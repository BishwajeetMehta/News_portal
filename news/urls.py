from django.urls import path
from .views import AboutPageView,CategoryPageView,ContactUsPageView,Description
urlpatterns = [
   
     path('about', AboutPageView.as_view(), name='about'),
     path('categories',CategoryPageView.as_view(),name='categories'),
     path('contactus',ContactUsPageView.as_view(), name='contactus'),
     path('description/<int:id>',Description.as_view(),name="Description"),
     
]
