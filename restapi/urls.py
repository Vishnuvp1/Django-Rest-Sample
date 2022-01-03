from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.RegisterAV.as_view(), name='register'),

    path('users/', views.UsersAV.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
