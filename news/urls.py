from django.urls import path
from .views import AboutPageView,CategoryPageView,LatestNewsPageView,ContactUsPageView,HomePageView 

urlpatterns = [
   
     path('about', AboutPageView.as_view(), name='about'),
     path('categories',CategoryPageView.as_view(),name='categories'),
     path('latestnews',LatestNewsPageView.as_view(), name='latest_news'),
     path('contactus',ContactUsPageView.as_view(), name='contactus')
]
