from django.urls import path, include
from .views import CategoryViewSet,NewsViewSet,NewsDetailView

urlpatterns = [

    path('auth/', include('rest_framework.urls')),
    path('category',CategoryViewSet.as_view()),
    path('news',NewsViewSet.as_view()),
    path('news/<int:pk>',NewsDetailView.as_view())
]
