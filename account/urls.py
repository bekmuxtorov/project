from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    # Verify code
    path('sent_code/', views.sent_verification_code),
    path('verify_code/', views.verify_code),

    # Register
    path('auth/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),

    path('auth/register/karer/', views.KarerRegisterAPIView.as_view()),
    path('auth/register/tax_officer/', views.TaxOfficerRegisterAPIView.as_view()),
    # Region
    path('regions/create/', views.RegionCreateAPIView.as_view()),
    path('regions/', views.RegionListAPIView.as_view()),
    path('regions/<int:pk>/', views.RegionDetailAPIView.as_view()),
    path('regions/<int:pk>/update/', views.RegionUpdateAPIView.as_view()),
    path('regions/<int:pk>/delete/', views.RegionDeleteAPIView.as_view()),

]
