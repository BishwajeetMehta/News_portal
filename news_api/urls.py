from django.urls import path, include
from .views import CategoryViewSet,NewsViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [

    path('auth/', include('rest_framework.urls')),
    path('category',CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>',CategoryViewSet.as_view({'get': 'retrieve'})),
    path('news',NewsViewSet.as_view({'get': 'list'})),
    path('news/<int:pk>',NewsViewSet.as_view({'get': 'retrieve'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
